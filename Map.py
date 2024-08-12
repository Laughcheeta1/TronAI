import random


class Tron_Map:
    def __init__(self, width=6, height=6, num_players=2):
        self._width = width
        self._height = height
        self._num_players = num_players
        self._map = [[0 for x in range(width)] for y in range(height)]

        self._current_player = 1
        self._positions = [[random.randint(0, width - 1), random.randint(0, height - 1)] for _ in range(num_players)]

    def get_map(self):
        return self._map

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

