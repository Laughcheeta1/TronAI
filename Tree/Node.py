import numpy as np

class Node ():
  def __init__(self, state,value,operators,operator=None, parent=None,objective=None):
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

  def add_child(self, value, state, operator):
    node=type(self)(value=value, state=state, operator=operator,parent=self,operators=self.operators)
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  def add_node_child(self, node):
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  #Devuelve todos los estados según los operadores aplicados
  def getChildren(self):
    return [
        self.getState(i)
          if not self.repeatStatePath(self.getState(i))
            else None for i, op in enumerate(self.operators)]

  def getState(self, index):
    pass

  def __eq__(self, other):
    return self.state == other.state

  def repeatStatePath(self, state):
      n=self
      while n is not None and n.state!=state:
          n=n.parent
      return n is not None

  def pathObjective(self):
      n=self
      result=[]
      while n is not None:
          result.append(n)
          n=n.parent
      return result

  def heuristic(self):
    return 0

  # By default we are going to state that two nodes are equal if their states are the same. 
  # Each inidivual implementation can overwrite this function if needed
  def isObjective(self):
    return (self.state==self.objetive.state)
