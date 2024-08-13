import random
import Constants


class TronMap:
    def __init__(self, width=6, height=6, num_players=2):
        """
        Constructor of the class

        Parameters
        ----------
        width
        height
        num_players
        """
        self._width = width
        self._height = height

        if num_players > width * height / 2:
            raise Exception("Invalid number of players for the size")

        self._num_players = num_players
        self._map = [[0 for x in range(width)] for y in range(height)]

        self._current_player = 1
        self._positions = self._generate_random_positions()

        # we put map[y][x] because in the structure defined in line 14,
        # each row y contains the columns x
        for i, pos in enumerate(self._positions):
            self._map[pos[1]][pos[0]] = i + 1

    def get_map(self) -> list[list[int]]:
        """
        Get the map of the game

        Returns
        -------
            The matrix representing the map of the game, where the first dimension are all the rows and the second
            dimension are all the columns. That is: map[y][x] will return the value of the position (x, y) in the map.
        """
        return self._map

    def get_players_positions(self) -> list[tuple[int, int]]:
        """
        Get the positions of all the players

        Returns
        -------
            A list of tuples with the positions of the players, where the i - 1 index represents the position
            of the ith player.

            The first number in the tuple is the x coordinate (column) and the second one is the y coordinate (row)

            Ex: the position of the player 1 will be stored in the index 0 of the list
        """
        return self._positions

    def get_player_position(self, player) -> tuple[int, int]:
        """
        Get the position of a specific player

        Parameters
        ----------
        player
            The number of the player you want to get the position of
            Ex: 1 for player 1

        Returns
        -------
            Tuple with the x (column) and y (row) coordinates of the player correspondingly
        """
        return self._positions[player - 1]

    def print_map(self) -> None:
        """
        Prints the map of the game in the console

        Returns
        -------
            None
        """
        for row in self._map:
            print(row)

    def get_available_moves(self) -> tuple[int, int]:
        """
        Get the available moves for the current player (Includes the ones that will cause death)

        Returns
        -------
            A generator with all the possible moves that the player can make as a tuple (x, y)
        """
        player_position = self._positions[self._current_player - 1]

        if player_position[1] - 1 >= 0:
            yield player_position[0], player_position[1] - 1

        # Lower one
        if player_position[1] + 1 < self._height:
            yield player_position[0], player_position[1] + 1

        # Left one
        if player_position[0] - 1 >= 0:
            yield player_position[0] - 1, player_position[1]

        # Right one
        if player_position[0] + 1 < self._width:
            yield player_position[0] + 1, player_position[1]

    def game_finished(self) -> bool:
        """
        Check if the game has finished or not

        Returns
        -------
            boolean
        """
        return self._num_players == 1

    def add_move(self, x: int, y: int) -> tuple[int, str]:
        """
        Make a move in the game. The move will automatically will be made by the current player, that is, the player
        that has the turn at the moment.
        It will return both a status of the move, and a message of the result of the move.

        The status is meant to be operated for by the developer, the message is meant to be shown to the user.

        All the possible status can be found in the Constants.py file

        Parameters
        ----------
        x: the column coordinate of the move
        y: the row coordinate of the move

        Returns
        -------
            A tuple with the first element being the status of the move and the second element being
            a string with a message of the move.
        """
        if message := self._check_invalid_move(x, y):
            return Constants.INVALID, message

        if killer := self._check_player_dead(x, y):  # Player stepped in a trail of another player
            self._num_players -= 1
            return Constants.PLAYER_DEAD, self._get_death_message(killer)

        self._map[y][x] = self._current_player
        self._positions[self._current_player - 1] = (x, y)
        self._next_player()
        return Constants.VALID, "Move was valid"

    def count_reachable_spaces(self, player: int, steps: int = 3) -> int:
        """
        Count the amount of reachable spaces (that do not generate death) that a player has in
        a certain amount of steps

        Parameters
        ----------
        player: the number of the player
        steps: amount of steps to calculate the reachable spaces, default to 3

        Returns
        -------
            Integer representing the amount of reachable spaces

        """
        if player <= 0 or player > self._num_players:
            raise Exception("That is not a valid player")

        queue = [self._positions[player - 1]]
        visited = set()  # Set because searching in a set is O(1)

        """
        This will make sure that we only go through the
        steps we want, because the first layer, is going to be passed through in the first loop,
        the second layer in the second loop, and so on and so forth. 
        
        When we finish the loop, we will still have the last layer in the queue, so we will add it to the visited set.
        """
        for _ in range(steps):
            for place in queue.copy():
                for neighbour in self._get_safe_moves(place):
                    if neighbour not in queue and neighbour not in visited:
                        queue.append(neighbour)

                queue.pop(0)
                visited.add(place)

        visited.update(queue)

        # -1 to account for adding the current place at first
        return len(visited) - 1

    def _get_safe_moves(self, place) -> tuple[int, int]:
        """
        Get the safe moves from a certain place in the map

        Parameters
        ----------
        place

        Returns
        -------
            A generator with all the safe moves from the place in a tuple(x, y)

        """
        # Upper one
        if place[1] - 1 >= 0 and self._map[place[1] - 1][place[0]] == 0:
            yield place[0], place[1] - 1

        # Lower one
        if place[1] + 1 < self._height and self._map[place[1] + 1][place[0]] == 0:
            yield place[0], place[1] + 1

        # Left one
        if place[0] - 1 >= 0 and self._map[place[1]][place[0] - 1] == 0:
            yield place[0] - 1, place[1]

        # Right one
        if place[0] + 1 < self._width and self._map[place[1]][place[0] + 1] == 0:
            yield place[0] + 1, place[1]

    def _next_player(self) -> None:
        self._current_player = (self._current_player % self._num_players) + 1

    def _generate_random_positions(self) -> list[tuple[int, int]]:
        positions = []

        for _ in range(self._num_players):
            rand_pos = (random.randint(0, self._width - 1), random.randint(0, self._height - 1))

            while self._map[rand_pos[0]][rand_pos[1]] != 0:
                rand_pos = (random.randint(0, self._width), random.randint(0, self._height))

            positions.append(rand_pos)  # Return the current random position (honestly used yield just because)

        return positions

    def _check_invalid_move(self, x: int, y: int) -> str:
        current_position = self._positions[self._current_player - 1]

        if (movement_x := abs(x - current_position[0])) > 1 or (movement_y := abs(y - current_position[1])) > 1:
            return "Cannot move further than one square at a time"

        if movement_x == 1 and movement_y == 1:
            return "Cannot move diagonally"

        # It is moving to the current position of a player
        return ""

    def _check_player_dead(self, x: int, y: int) -> int:
        # If the position in the map is cero that means no one was there, therefore the player is safe
        # (in python 0 is a falsy value, that means "if 0" will result in NOT executing the if statement)
        return self._map[y][x]

    def _get_death_message(self, killer: int):
        return f"Player {self._current_player} was killed by Player {killer}"
