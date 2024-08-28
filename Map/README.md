# Why this README?
To explain the Map folder

# Constants.py
This is the smallest file, it just contains constant status codes for the 
results of making moves in the map. They are meant to be used by the developer.

# Map.py
This is the main file of the Map folder. It contains the Map class, which is
where all the logic of the tron game (or more like our version of it) happens.

Is important to note that all the coordinates al handled in an `(x, y)` format, 
where <b>x</b> is the row and <b>y</b> is the column; and just like in UI design (0, 0) is the top left,
that means, the numbers grow from left to right and from top to bottom (a cartesian plane inverted
in the x-axis).

The Map class has the following public methods:
- `get_current_player(self) -> int`: returns the player that has the turn.
- `__init__(self, width=6, height=6, num_players=2)`: Constructor, initializes the map.
- `def get_map(self) -> list[list[int]]`: returns the matrix representing the map of the game.
- `def get_players_positions(self) -> list[tuple[int, int]]`: returns the positions of all players as a list of tuples.
- `get_player_position(self, player) -> tuple[int, int]`: returns the position of a specific player as a tuple.
-  `print_map(self) -> None`: prints the map to the console.
-  `get_available_moves(self) -> tuple[int, int]`: returns the available moves for the current player, that is, the
    player that has the turn.
-  `game_finished(self) -> bool`: returns True if the game has come to an end, False otherwise.
-  `add_move(self, x: int, y: int) -> tuple[int, str]`: makes a move for the current player. After making the move, automatically the turn will be passed to the next player.
-  `count_reachable_spaces(self, player: int, steps: int = 3) -> int`: returns the number of reachable spaces for a 
    player in a certain number of steps (Supposes that the opponent is not going to move, this is for the heuristic of 
    the game).
- `check_player_dead(self, x: int, y: int) -> int`: it returns if a move that a player makes, will result in its death. 
    It returns 0 if the player is not dead, otherwise it returns the player that killed it.
    (Remember that in python, 0 is a falsy value and any other number is truthy value, therefore the function can be used as a boolean for if statements).

For more detailed information check the actual methods, they are well documented.