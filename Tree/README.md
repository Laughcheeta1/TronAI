# Why this README?

To explain the Tree module

## Node.py

This file contains the Node class. It is meant to be used for inheritance to use the Tree class in an implementation inside a game for the AlphaBeta algorithm.

The Node class has the following methods:

1. `__init__(self, state: Any, value: Any, operators: List, operator: Any = None, parent: Node = None, Objective: Node = None) -> None`

   - Initializes a Node
   - **Parameters:**
     - `state`: The state of the node.
     - `value`: The value stored in the node.
     - `operators`: A list of operators to determine future children.
     - `operator`: Operator used to create this node.
     - `parent`: Parent node.
     - `objective`: Node representing the ideal state.
   - **Returns:** None

2. `add_child(self, value: Any, state: Any, operator: Any)`

   - Adds a child node to the current node.
   - **Parameters:**
     - `value`: The value of the child node.
     - `state`: The state of the child node.
     - `operator`: The operator that leads to the child node.
   - **Returns:** None

3. `add_node_child(self, node: Node)`

   - Adds a child node to the current node.
   - **Parameters:**
     - `value`: The value of the child node.
     - `state`: The state of the child node.
     - `operator`: The operator that leads to the child node.
   - **Returns:** None

4. `getChildren(self) -> List`

   - Returns all the possible children of a node.
   - **Returns:** A list of states representing the states of the children nodes.

5. `getState(self, index: int) -> index`

   - Method to be implemented by any custom implementation of the node class. It returns the state of a specific operator inside the operators list.
   - **Parameters:**
     - `index`: The index of the operator for which the state is to be returned.
   - **Returns:** The state of a specified operator.

6. `__eq__(self, other: Node) -> bool`

   - Method overriding '==' verifications.
   - **Parameters:**
     - `other`: Node to be compared.
   - **Returns:** Wether the nodes are equal or not.

7. `repeatStatePath(self, state: Any) -> bool`

   - Method that checks if a specific state has already existed.
   - **Parameters:**
     - `state`: State to be checked.
   - **Returns:** Wether the state has already existed or not.

8. `pathObjective(self) -> List['Node']`

   - Returns the path from the current node to the root node.
   - **Returns:** A list of nodes representing the path from the current node to the root node.

9. `heuristic(self) -> int`

   - Returns a heuristic value for the node.
   - **Returns:** 0 (default implementation)

10. `isObjective(self) -> bool`

- Checks if the current node's state matches the objective's state.
- **Returns:** True if the current node's state matches the objective's state, False otherwise.

## Tree.py

This file contains the Tree class, which is where all the logic of our version of the AlphaBeta algorithm happens.

The Tree class has the following public methods:

1. `__init__(self, root: Node, operators: List[str]) -> None`

   - Initializes the Tree with a root node and a list of operators.
   - **Parameters:**
     - `root`: The root node of the tree.
     - `operators`: A list of operators available for the tree.
   - **Returns:** None

2. `printPath(self, n: Node) -> List[Node]`

   - Prints the path from the given node to the root node and returns the path.
   - **Parameters:**
     - `n`: The node from which to start the path.
   - **Returns:** A list of nodes representing the path from the given node to the root node.

3. `reinitRoot(self) -> None`

   - Reinitializes the root node by resetting its operator, parent, objective, children, and level.
   - **Returns:** None

4. `alfaBeta(self, depth: int, maxPlayer: bool = True) -> Node`

   - Performs the AlphaBeta pruning algorithm to determine the best move.
   - **Parameters:**
     - `depth`: The depth to which the algorithm should search.
     - `maxPlayer`: Boolean indicating if the current move is by the maximizing player (default is True).
   - **Returns:** The node representing the best move.

5. `alfaBetaR(self, node: Node, depth: int, maxPlayer: bool, alpha: float, beta: float) -> tuple[float, float]`
   - Recursively performs the AlphaBeta pruning algorithm.
   - **Parameters:**
     - `node`: The current node being evaluated.
     - `depth`: The current depth in the tree.
     - `maxPlayer`: Boolean indicating if the current move is by the maximizing player.
     - `alpha`: The alpha value for pruning.
     - `beta`: The beta value for pruning.
   - **Returns:** A tuple containing the alpha and beta values.
