# Why this README?

To explain the AI **module**

## TronTree.py

This file contains the TronTree class. It is used to represent the decision tree for the Tron game, extending the base Tree class from the [Tree](../Tree/README.md) module.

The TronTree class has the following methods:

1. `__init__(self, game, objective, maxPlayer)`

   - Initializes the TronTree with a root node and an objective for the game, as well as a boolean indicating if the player is Max or Min.
   - **Parameters:**
     - `game`: The game object to be used for the tree.
     - `objective`: The objective for the game (e.g., win for Max or Min).
     - `maxPlayer`: Boolean indicating if the player is Max (True) or Min (False).
   - **Returns:** None

## TronNode.py

This file contains the TronNode class. It represents a node in the decision tree for the Tron game, extending the base Node class from the [Tree](../Tree/README.md) module.

The TronNode class has the following methods:

1. `__init__(self, **kwargs)`

   - Initializes a TronNode with a state, value, game, objective, and player.
   - **Parameters:**
     - `kwargs`: Additional keyword arguments passed to the parent Node class.
   - **Returns:** None

2. `updateGame(self)`

   - Updates the game object with the current state of the node.
   - **Returns:** None

3. `getState(self, index: int) -> Optional[List[List[str]]]`

   - Returns the next state of the board after applying the operator at the given index.
   - **Parameters:**
     - `index`: The index of the operator to apply.
   - **Returns:** The next state of the board if the move is valid, otherwise None.

4. `heuristic(self) -> int`

   - Returns a heuristic value for the node based on the state of the board.
   - **Returns:** 1 if the state is a win for Max, -1 if the state is a win for Min, 0 if the state is a draw or non-terminal.

5. `isObjective(self) -> bool`

   - Returns whether the node is an objective node or not.
   - **Returns:** True if the node is an objective node, False otherwise.

6. `createOperators(self) -> List`

   - Returns all the possible operators for the current node.
   - **Returns:** A list of operators available for the current node.
