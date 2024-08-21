from Tree import Node
import numpy as np
from Map.Map import TronMap

class TronNode(Node):

  def __init__(self, **kwargs) -> None:
    """
    Initializes a TronNode with a state, value, game, objective, and player.
    Objective attribute for this implementation represents the player that is trying to win Max(True) or Min(False).
    
    Parameters:
    - kwargs: Additional keyword arguments passed to the parent Node class.
    
    Returns: None
    """
    super(TronNode, self).__init__(**kwargs)
    self.operators = self.createOperators()
    self.game: TronMap = self.game
    self.updateGame()

  def updateGame(self) -> None:
    """
    Updates the game object with the current state of the node.
    
    Returns: None
    """
    activePlayerIndex = 1 if self.player else 0
    self.game.add_move(self.state[activePlayerIndex][0], self.state[activePlayerIndex][1])

  def getState(self, index: int) -> list | None:
    """
    Returns the next state of the board after applying the operator at the given index.
    
    Parameters:
    - index: The index of the operator to apply.
    
    Returns: The next state of the board if the move is valid, otherwise None.
    """
    if index < len(self.operators):
      return self.operators[index]
    return None

  def heuristic(self) -> int:
    """
    Returns a heuristic value for the node based on the state of the board.
    
    Returns: 1 if the state is a win for Max, -1 if the state is a win for Min, 0 if the state is a draw or non-terminal.
    """
    # TODO: implement custom heuristic for the Tron game
    
    # Temporary heuristic
    # Check if max is dead and return -1
    if self.game._check_player_dead(self.state[0][0], self.state[0][1]):
      return -1
    
    # Check if min is dead and return 1
    if self.game._check_player_dead(self.state[1][0], self.state[1][1]):
      return 1
    
    # Return 0 if the game is not over
    return 0
  
  def isObjective(self) -> bool:
    """
    Returns wether the node is an objective node or not.
    
    Returns: True if the node is an objective node, False otherwise.
    """


    # FIXME: This method is not working properly due to the position where a player is being technically already occupied, the following is a temporary workaround
    return False if self.game._num_players > 1 else True

    # Objective determines if we are looking for a Max win or a Min win

    # If we are looking for a Max win, we check if Min is dead
    if self.objective:
      return self.game._check_player_dead(self.state[1][0], self.state[1][1])
    
    # If we are looking for a Min win, we check if Max is dead
    if not self.objective:
      return self.game._check_player_dead(self.state[0][0], self.state[0][1])
  
  def createOperators(self) -> list:
    """
    Returns all the possible operators for the current node.
    
    Returns: A list of operators available for the current node.
    """

    operators = []
    activePlayerIndex = 0 if self.player else 1
    inactivePlayerIndex = 1 if self.player else 0

    tempOperator = [0, 0]
    for operator in self.game._get_safe_moves(self.state[activePlayerIndex]):
      tempOperator[activePlayerIndex] = operator
      tempOperator[inactivePlayerIndex] = self.state[inactivePlayerIndex]
      operators.append(tempOperator)
    
    return operators
