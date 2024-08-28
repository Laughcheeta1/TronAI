# Why this README?

To explain the Tree module

## Node.py

This file contains the Node class. It is a base class for creating nodes in a decision tree.

The Node class has the following methods:

1. `__init__(self, state, value, game, objective, player: bool = True, operators=None, operator=None, parent=None)`

   - Initializes a Node.
   - **Parameters:**
     - `state`: The state of the node.
     - `value`: The value stored in the node.
     - `game`: The game object associated with the node.
     - `objective`: The objective state for the node.
     - `player`: Boolean indicating if the player is Max (True) or Min (False).
     - `operators`: A list of operators to determine future children.
     - `operator`: Operator used to create this node.
     - `parent`: Parent node.
   - **Returns:** None

2. `add_child(self, value, state, operator) -> None`

   - Adds a child node to the current node.
   - **Parameters:**
     - `value`: The value of the child node.
     - `state`: The state of the child node.
     - `operator`: The operator that leads to the child node.
   - **Returns:** None

3. `add_node_child(self, node) -> None`

   - Adds a child node to the current node.
   - **Parameters:**
     - `node`: The child node to be added.
   - **Returns:** None

4. `getChildren(self) -> list`

   - Returns all the possible children of a node.
   - **Returns:** A list of states representing the states of the children nodes.

5. `getState(self, index)`

   - Method to be implemented by any custom implementation of the node class. It returns the state of a specific operator inside the operators list.
   - **Parameters:**
     - `index`: The index of the operator for which the state is to be returned.
   - **Returns:** The state of a specified operator.

6. `__eq__(self, other) -> bool`

   - Method overriding '==' verifications.
   - **Parameters:**
     - `other`: Node to be compared.
   - **Returns:** Whether the nodes are equal or not.

7. `repeatStatePath(self, state) -> bool`

   - Method that checks if a specific state has already existed.
   - **Parameters:**
     - `state`: State to be checked.
   - **Returns:** Whether the state has already existed or not.

8. `pathObjective(self) -> list['Node']`

   - Returns the path from the current node to the root node.
   - **Returns:** A list of nodes representing the path from the current node to the root node.

9. `heuristic(self) -> int`

   - Returns a heuristic value for the node.
   - **Returns:** 0 (default implementation)

10. `isObjective(self) -> bool`

    - Method to be implemented by any custom implementation of the node class. It returns whether the node is the objective node or not.
    - **Returns:** True if the node is an objective node, False otherwise.

11. `createOperators(self) -> list`

    - Method to be implemented by any custom implementation of the node class. It returns the list of operators for the node.
    - **Returns:** A list of operators.

## Tree.py

This file contains the Tree class. It is used to represent the decision tree for a game, extending the base Node class.

The Tree class has the following methods:

1. `__init__(self, game, objective) -> None`

   - Initializes the Tree with a root node and an objective for the game.
   - **Parameters:**
     - `game`: The game object to be used for the tree.
     - `objective`: The objective for the game (e.g., win for Max or Min).
   - **Returns:** None

2. `printPath(self, n) -> list[str]`

   - Prints the path from the given node to the root node and returns the path.
   - **Parameters:**
     - `n`: The node from which to start the path.
   - **Returns:** A list of nodes representing the path from the given node to the root node.

3. `reinitRoot(self) -> None`

   - Reinitializes the root node by resetting its operator, parent, objective, children, and level.
   - **Returns:** None

4. `alphaBeta(self, depth, maxPlayer=True) -> Node`

   - Performs the AlphaBeta pruning algorithm to determine the best move.
   - **Parameters:**
     - `depth`: The depth to which the algorithm should search.
     - `maxPlayer`: Boolean indicating if the current move is by the maximizing player (default is True).
   - **Returns:** The node representing the best move.

5. `alphaBetaR(self, node: Node, depth, maxPlayer, alpha, beta) -> tuple[int, int]`

   - Recursively performs the AlphaBeta pruning algorithm.
   - **Parameters:**
     - `node`: The current node being evaluated.
     - `depth`: The current depth in the tree.
     - `maxPlayer`: Boolean indicating if the current move is by the maximizing player.
     - `alpha`: The alpha value for pruning.
     - `beta`: The beta value for pruning.
   - **Returns:** A tuple containing the alpha and beta values.
