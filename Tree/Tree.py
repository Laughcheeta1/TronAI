from .Node import Node
import numpy as np

class Tree ():
  def __init__(self, root ,operators) -> None:
    """
    Initializes the Tree with a root node and a list of operators.
    
    Parameters:
    - root: The root node of the tree.
    - operators: A list of operators available for the tree.
    
    Returns: None
    """
    self.root=root
    self.operators=operators

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
            print(f'operador:  {self.operators[node.operator]} \t estado: {node.state}')
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
    self.root.objective=None
    self.root.children = []
    self.root.level=0

  def alfaBeta(self, depth, maxPlayer = True) -> Node:
    """
    Performs the AlphaBeta pruning algorithm to determine the best move.
    
    Parameters:
    - depth: The depth to which the algorithm should search.
    - maxPlayer: Boolean indicating if the current move is by the maximizing player (default is True).
    
    Returns: The node representing the best move.
    """

    self.root.beta, self.root.alpha = self.alfaBetaR(self.root, depth-1, maxPlayer, -np.inf, np.inf)

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

  def alfaBetaR(self, node, depth, maxPlayer, alpha, beta) -> tuple[float, float]:
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
    if depth==0 or node.isObjective():
      if maxPlayer:
        node.alpha=node.heuristic()
      else:
        node.beta=node.heuristic()
      return node.alpha, node.beta
    
    # Generate node children
    children=node.getChildren()

    # Max player
    if maxPlayer:
      for i,child in enumerate(children):
        if child is not None:
          newChild=type(self.root)(value=node.value+'-'+str(i),state=child,operator=i,parent=node,
                                   operators=node.operators,player=False)
          newChild=node.add_node_child(newChild)
          alpha=max(alpha,self.alfaBetaR(newChild,depth-1,False, alpha, beta)[1])
          newChild.alpha = alpha
          newChild.beta = beta
          if alpha>=beta:
            break

    else: # Min player
      for i,child in enumerate(children):
        if child is not None:
          newChild=type(self.root)(value=node.value+'-'+str(i),state=child,operator=i,parent=node,
                                   operators=node.operators,player=True)
          newChild=node.add_node_child(newChild)
          beta=min(beta,self.alfaBetaR(newChild,depth-1,True, alpha, beta)[0])
          newChild.alpha = alpha
          newChild.beta = beta
          if alpha>=beta:
            break

    node.alpha = alpha
    node.beta = beta
    return alpha, beta
