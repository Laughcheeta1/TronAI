from . import Node
import numpy as np

class Tree ():
  def __init__(self, game, objective) -> None:
    """
    Initializes the Tree with a root node and an objective for the game.
    
    Parameters:
    - game: The game object to be used for the tree.
    - objective: The objective for the game (e.g., win for Max or Min).

    Returns: None
    """
    self.game=game
    self.objective=objective
    self.root: Node = type(self).rootNode(game=game, objective=objective)

  def printPath(self,n) -> list[str]:
    """
    Prints the path from the given node to the root node and returns the path.
    
    Parameters:
    - n: The node from which to start the path.
    
    Returns: A list of nodes representing the path from the given node to the root node.
    """
    stack=n.pathObjective()
    path=stack.copy()
    while len(stack)!=0:
        node=stack.pop()
        if node.operator is not None:
            print(f'operador:  {node.operator} \t estado: {node.state}')
        else:
            print(f' {node.state}')
    return path

  def reinitRoot(self) -> None:
    """
    Reinitializes the root node by resetting its operator, parent, objective, children, and level.
    
    Returns: None
    """
    self.root.operator=None
    self.root.parent=None
    self.root.objective=self.objective
    self.root.game=self.game
    self.root.children = []
    self.root.level=0

  def alphaBeta(self, depth, maxPlayer = True) -> Node:
    """
    Performs the AlphaBeta pruning algorithm to determine the best move.
    
    Parameters:
    - depth: The depth to which the algorithm should search.
    - maxPlayer: Boolean indicating if the current move is by the maximizing player (default is True).
    
    Returns: The node representing the best move.
    """
    # TODO: Change parameters to self.root.alpha and self.root.beta
    self.root.beta, self.root.alpha = self.alphaBetaR(self.root, depth, maxPlayer, self.root.alpha, self.root.beta)

    if maxPlayer:
      # Compare all children of root and find the one with the maximum alpha
      values=[c.alpha for c in self.root.children]
      maxAlpha=max(values)
      index=values.index(maxAlpha)

    else:
      # Compare all children of root and find the one with the minimum beta
      values=[c.beta for c in self.root.children]
      minBeta=min(values)
      index=values.index(minBeta)

    return self.root.children[index]

  def alphaBetaR(self, node: Node, depth, maxPlayer, alpha, beta) -> tuple[int, int]:
    """
    Recursively performs the AlphaBeta pruning algorithm.
    
    Parameters:
    - node: The current node being evaluated.
    - depth: The current depth in the tree.
    - maxPlayer: Boolean indicating if the current move is by the maximizing player.
    - alpha: The alpha value for pruning.
    - beta: The beta value for pruning.
    
    Returns: A tuple containing the alpha and beta values.
    """
    if depth == 0 or node.isObjective():
      if maxPlayer:
        node.alpha = node.heuristic()
      else:
        node.beta = node.heuristic()
      return node.alpha, node.beta
    
    # Generate node children
    children=node.getChildren()

    # Max player
    if maxPlayer:
      for i,child in enumerate(children):
        if child is not None:
          newChild = type(self.root)(value = node.value+'-'+str(i), state = child,operator=i, parent = node,
                                      objective = self.objective, game = node.game, player=False)
          newChild = node.add_node_child(newChild)
          alpha = max(alpha,self.alphaBetaR(newChild,depth-1,False, alpha, beta)[1])
          newChild.alpha = alpha
          newChild.beta = beta
          if alpha >= beta:
            break

    else: # Min player
      for i,child in enumerate(children):
        if child is not None:
          newChild = type(self.root)(value = node.value+'-'+str(i), state = child, operator = i, parent = node,
                                      objective = self.objective, game = node.game, player = True)
          newChild = node.add_node_child(newChild)
          beta = min(beta,self.alphaBetaR(newChild,depth-1,True, alpha, beta)[0])
          newChild.alpha = alpha
          newChild.beta = beta
          if alpha >= beta:
            break

    node.alpha = alpha
    node.beta = beta
    return alpha, beta
