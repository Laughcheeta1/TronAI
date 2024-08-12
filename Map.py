import random


class Tron_Map:
    def __init__(self, width=6, height=6, num_players=2):
        self._width = width
        self._height = height

        if (num_players > width * height / 2):
            print("Invalid number of players for the size")
            raise()  # TODO

        self._num_players = num_players
        self._map = [[0 for x in range(width)] for y in range(height)]

        self._current_player = 1
        self._positions = self._generate_random_positions()
        
        for i, pos in enumerate(self._positions):
            self._map[pos[0]][pos[1]] = i + 1

    def get_map(self):
        return self._map

    def print_map(self):
        for row in self._map:
            print(row)

    def add_move(self, x, y):
        self._map[y][x] = self._current_player
        self._positions[self._current_player - 1] = (x, y)
        self._next_player()

    def get_players_positions(self):
        return self._positions

    def get_player_position(self, player):
        return self._positions[player -1]

    def _next_player(self):
        self._current_player = (self._current_player % self._num_players) + 1

    def _generate_random_positions(self):
        positions = []

        for _ in range(self._num_players):
            rand_pos = (random.randint(0, self._width - 1), random.randint(0, self._height - 1))

            while self._map[rand_pos[0]][rand_pos[1]] != 0:
                rand_pos = (random.randint(0, self._width), random.randint(0, self._height))

            positions.append(rand_pos)  # Return the current random position (honestly used yield just because)

        return positions
