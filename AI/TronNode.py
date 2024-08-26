from Tree import Node
import numpy as np
from Map.Map import TronMap

class TronNode(Node):

  def __init__(self, root: bool = False, **kwargs) -> None:
    """
    Initializes a TronNode with a state, value, game, objective, and player.
    Objective attribute for this implementation represents wether a player won or lost.
    
    Parameters:
    - kwargs: Additional keyword arguments passed to the parent Node class.
    
    Returns: None
    """
    super(TronNode, self).__init__(**kwargs)
    self.game: TronMap = self.game
    self.whomWasItThatKilledMax = self.game.check_player_dead(self.state[0][0], self.state[0][1])
    self.whomWasItThatKilledMin = self.game.check_player_dead(self.state[1][0], self.state[1][1])
    # print("State: ", self.state, "Is player: ", self.player, ", Max died: ", self.whomWasItThatKilledMax, "Min died: ", self.whomWasItThatKilledMin, "Player count: ", self.game._num_players)
    if not root:
      self.updateGame()
    self.operators = self.createOperators()

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
    
    
    # Check reachable spaces for each player
    heuristic = self.level if self.player else -self.level
    
    # Check if a player died
    if self.whomWasItThatKilledMax != 0 and self.whomWasItThatKilledMin != 0:
      # Check which player died
      if self.player:
        # print("Min died", self.state, "Player: ", self.player)
        return heuristic + self.game._height * self.game._width
      else:
        # print("Max died", self.state, "Player: ", self.player)
        return heuristic - self.game._height * self.game._width

    heuristic += self.game.count_reachable_spaces(1, 4)
    heuristic -= self.game.count_reachable_spaces(2, 4)
    return heuristic
  
  def isObjective(self) -> bool:
    """
    Returns wether the node is an objective node or not.
    
    Returns: True if the node is an objective node, False otherwise.
    """

    if self.whomWasItThatKilledMax != 0 and self.whomWasItThatKilledMin != 0:
      return True
    
    return False
  
  def createOperators(self) -> list:
    """
    Returns all the possible operators for the current node.
    
    Returns: A list of operators available for the current node.
    """

    operators = []
    activePlayerIndex = 0 if self.player else 1
    inactivePlayerIndex = 1 if self.player else 0

    
    for operator in self.game.get_available_moves():
      tempOperator = [0, 0]
      tempOperator[activePlayerIndex] = operator
      tempOperator[inactivePlayerIndex] = self.state[inactivePlayerIndex]
      operators.append(tempOperator)
    
    return operators
