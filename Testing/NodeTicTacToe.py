from Tree.Node import Node
import numpy as np

class NodeTicTacToe(Node):
  """
    This class is used exclusively for testing with the tic-tac-toe game
  """

  def __init__(self, player: bool = True, **kwargs) -> None:
    """
    Initializes a NodeTicTacToe with a player indicator and other keyword arguments.
    
    Parameters:
    - player: Boolean indicating if the player is Max (True) or Min (False).
    - kwargs: Additional keyword arguments passed to the parent Node class.
    
    Returns: None
    """
    super(NodeTicTacToe, self).__init__(**kwargs)
    self.player=player
    self.alpha=float('-inf')
    self.beta=float('inf')

  def getState(self, index: int) -> list[list[str]] | None:
    """
    Returns the next state of the board after applying the operator at the given index.
    
    Parameters:
    - index: The index of the operator to apply.
    
    Returns: The next state of the board if the move is valid, otherwise None.
    """
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

  def isObjective(self) -> bool:
    """
    Checks if the current node's state is an objective state (win or draw).
    
    Returns: True if the current node's state is an objective state, False otherwise.
    """
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

  def heuristic(self) -> int:
    """
    Returns a heuristic value for the node based on the state of the board.
    
    Returns: 1 if the state is a win for Max, -1 if the state is a win for Min, 0 if the state is a draw or non-terminal.
    """
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
