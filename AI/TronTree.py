from Tree import Tree
from . import TronNode
from Map.Map import TronMap

class TronTree(Tree):
  def __init__(self, game, objective, maxPlayer) -> None:
    """
    Initializes the TronTree with a root node and an objective for the game, as well as a boolean indicating if the player is Max or Min.
    
    Parameters:
    - game: The game object to be used for the tree.
    - objective: The objective for the game (e.g., win for Max or Min).
    - maxPlayer: Boolean indicating if the player is Max (True) or Min (False).

    Returns: None
    """
    self.game: TronMap = game
    self.objective=objective

    # Initialize the root node with the initial state of the game that was provided
    rootState = (game.get_player_position(1), game.get_player_position(2))

    self.root: TronNode = TronNode(state=rootState, value="inicio", game=game, objective=objective, player=maxPlayer)

