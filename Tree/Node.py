import numpy as np

class Node ():
  def __init__(self, state, value, operators, operator=None, parent=None, objective=None) -> None:
    """
    Initializes a Node.
    
    Parameters:
    - state: The state of the node.
    - value: The value stored in the node.
    - operators: A list of operators to determine future children.
    - operator: Operator used to create this node.
    - parent: Parent node.
    - objective: Node representing the ideal state.
    
    Returns: None
    """
    self.state= state
    self.value = value
    self.children = []
    self.parent=parent
    self.operator=operator
    self.objective=objective
    self.level=0
    self.operators=operators
    self.alpha=-np.inf # To be used by AlphaBeta
    self.beta=np.inf # To be used by AlphaBeta

  def add_child(self, value, state, operator) -> None:
    """
    Adds a child node to the current node.
    
    Parameters:
    - value: The value of the child node.
    - state: The state of the child node.
    - operator: The operator that leads to the child node.
    
    Returns: None
    """
    node=type(self)(value=value, state=state, operator=operator,parent=self,operators=self.operators)
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  def add_node_child(self, node) -> None:
    """
    Adds a child node to the current node.
    
    Parameters:
    - node: The child node to be added.
    
    Returns: None
    """
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  #Devuelve todos los estados según los operadores aplicados
  def getChildren(self) -> List:
    """
    Returns all the possible children of a node.
    
    Returns: A list of states representing the states of the children nodes.
    """
    return [
        self.getState(i)
          if not self.repeatStatePath(self.getState(i))
            else None for i, op in enumerate(self.operators)]

  def getState(self, index):
    """
    Method to be implemented by any custom implementation of the node class. It returns the state of a specific operator inside the operators list.
    
    Parameters:
    - index: The index of the operator for which the state is to be returned.
    
    Returns: The state of a specified operator.
    """
    pass

  def __eq__(self, other) -> bool:
    """
    Method overriding '==' verifications.
    
    Parameters:
    - other: Node to be compared.
    
    Returns: Whether the nodes are equal or not.
    """
    return self.state == other.state

  def repeatStatePath(self, state) -> bool:
    """
    Method that checks if a specific state has already existed.
    
    Parameters:
    - state: State to be checked.
    
    Returns: Whether the state has already existed or not.
    """
    n=self
    while n is not None and n.state!=state:
        n=n.parent
    return n is not None

  def pathObjective(self) -> list['Node']:
    """
    Returns the path from the current node to the root node.
    
    Returns: A list of nodes representing the path from the current node to the root node.
    """
    n=self
    result=[]
    while n is not None:
        result.append(n)
        n=n.parent
    return result
  
  def heuristic(self)-> int:
    """
    Returns a heuristic value for the node.
    
    Returns: 0 (default implementation)
    """
    return 0

  
  def isObjective(self) -> bool:
    """
    Checks if the current node's state matches the objective's state.
    
    Returns: True if the current node's state matches the objective's state, False otherwise.
    """
    return (self.state==self.objective.state)
