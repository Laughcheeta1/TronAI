import random
import Constants


class TronMap:
    def __init__(self, width=6, height=6, num_players=2):
        self._width = width
        self._height = height

        if num_players > width * height / 2:
            raise Exception("Invalid number of players for the size")  # TODO

        self._num_players = num_players
        self._map = [[0 for x in range(width)] for y in range(height)]

        self._current_player = 1
        self._positions = self._generate_random_positions()
        
        # we put map[y][x] because in the structure defined in line 14,
        # each row y contains the columns x
        for i, pos in enumerate(self._positions):
            self._map[pos[1]][pos[0]] = i + 1

    def get_map(self):
        return self._map

    def get_players_positions(self):
        return self._positions

    def get_player_position(self, player):
        return self._positions[player - 1]

    def print_map(self):
        for row in self._map:
            print(row)

    def get_available_moves(self):
        player_position = self._positions[self._current_player - 1]
        possible_moves = []

        # Given that theres only 4 moves that can be made, might as well just 
        # hard code them 

        # Upper one
        if (player_position[0], player_position[1] - 1) not in self._positions:
            possible_moves.append((player_position[0], player_position[1] - 1))

        # Lower one
        if (player_position[0], player_position[1] + 1) not in self._positions:
            possible_moves.append((player_position[0], player_position[1] + 1))

        # Left one 
        if (player_position[0] - 1, player_position[1]) not in self._positions:
            possible_moves.append((player_position[0] - 1, player_position[1]))

        # Right one
        if (player_position[0] + 1, player_position[1]) not in self._positions:
            possible_moves.append((player_position[0] + 1, player_position[1]))

        return possible_moves

    def game_finished(self):
        return self._num_players == 1

    def add_move(self, x: int, y: int) -> tuple[str, str]:
        if message := self._check_invalid_move(x, y):
            return Constants.INVALID, message

        if killer := self._check_player_dead(x, y):  # Player stepped in a trail of another player
            self._num_players -= 1
            return Constants.PLAYER_DEAD, self._get_death_message(killer)

        self._map[y][x] = self._current_player
        self._positions[self._current_player - 1] = (x, y)
        self._next_player()
        return Constants.VALID, "Move was valid"

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
        
        if abs(x - current_position[0]) > 1 or abs(y - current_position[1]) > 1:
            return "Cannot move further than one square at a time"

        # It is moving to the current position of a player
        return ""

    def _check_player_dead(self, x: int, y: int) -> int:
        # If the position in the map is cero that means no one was there, therefore the player is safe
        # (in python 0 is a falsy value, that means "if 0" will result in NOT executing the if statement)
        return self._map[y][x]

    def _get_death_message(self, killer: int):
        return f"Player {self._current_player} was killed by Player {killer}"
