# Why this README?

To explain the Testing module

## NodeTicTacToe.py

This file contains the NodeTicTacToe class. It is meant to be used for testing of the AlphaBeta algorithm as a custom implementation of the Node class from the [Tree](../Tree/README.md) module. This class has a few custom implementations of Node methods.

The NodeTicTacToe class has the following methods:

1. `__init__(self, player: bool = True, **kwargs)`

   - Initializes a NodeTicTacToe with a player indicator and other keyword arguments.
   - **Parameters:**
     - `player`: Boolean indicating if the player is Max (True) or Min (False).
     - `kwargs`: Additional keyword arguments passed to the parent Node class.
   - **Returns:** None

2. `getState(self, index: int) -> Optional[List[List[str]]]`

   - Returns the next state of the board after applying the operator at the given index.
   - **Parameters:**
     - `index`: The index of the operator to apply.
   - **Returns:** The next state of the board if the move is valid, otherwise None.

3. `isObjective(self) -> bool`

   - Checks if the current node's state is an objective state (win or draw).
   - **Returns:** True if the current node's state is an objective state, False otherwise.

4. `heuristic(self) -> int`
   - Returns a heuristic value for the node based on the state of the board.
   - **Returns:** 1 if the state is a win for Max, -1 if the state is a win for Min, 0 if the state is a draw or non-terminal.
