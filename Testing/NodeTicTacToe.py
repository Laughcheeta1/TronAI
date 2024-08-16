from Tree.Node import Node
import numpy as np

class NodeTicTacToe(Node):
  """
    This class is used exclusively for testing with the tic-tac-toe game
  """

  def __init__(self, player = True, **kwargs):
    super(NodeTicTacToe, self).__init__(**kwargs)
    self.player=player
    self.alpha=float('-inf')
    self.beta=float('inf')

  def getState(self, index):
    state=self.state
    nextState=None
    (x,y)=self.operators[index]
    if state[x][y]==' ':
      nextState= [f.copy() for f in state]
      if self.player==True: # If the player is Max, we write X
        nextState[x][y]='X'
      else: # If the player is Min, we write O
        nextState[x][y]='O'
    return nextState if state!=nextState else None

  # Check if the state node is the objective node for Min or Max
  def isObjective(self):
    a=[f.copy() for f in self.state]
    b=np.array(a).T
    a.append(np.diag(self.state))
    a.append(np.flipud(self.state).diagonal())
    a=np.array(a)
    c=np.concatenate((a,b),axis=0)
    for f in c:
      if f[0]!=' ' and all(x == f[0] for x in f):
        return True
    # Draw
    if not np.in1d([' '], self.state):
      return True
    return False

  # If it is an objective node, if X return 1, if O -1 and if not 0
  def heuristic(self):
    a=[f.copy() for f in self.state]
    b=np.array(a).T
    a.append(np.diag(self.state))
    a.append(np.flipud(self.state).diagonal())
    a=np.array(a)
    c=np.concatenate((a,b),axis=0)
    # Winning states for Max and Min
    for f in c:
      if f[0]!=' ' and all(x == f[0] for x in f):
        return 1 if f[0]=='X' else -1
    # Draw
    if not np.in1d([' '], self.state):
      return 0
    # Add more conditions to the heuristic if needed
    return 0
