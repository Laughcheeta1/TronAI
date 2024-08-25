from Tree import Tree
from . import TronNode
from Map.Map import TronMap

class TronTree(Tree):
  def __init__(self, game, maxPlayer) -> None:
    """
    Initializes the TronTree with a root node and an objective for the game, as well as a boolean indicating if the player is Max or Min.
    
    Parameters:
    - game: The game object to be used for the tree.
    - objective: The objective for the game (e.g., win for Max or Min).
    - maxPlayer: Boolean indicating if the player is Max (True) or Min (False).

    Returns: None
    """

    # TODO: add difficulty parameter to the constructor, and to the nodes
    self.game: TronMap = game

    # Initialize the root node with the initial state of the game that was provided
    rootState = (self.game.get_player_position(1), self.game.get_player_position(2))

    self.root: TronNode = TronNode(root=True, state=rootState, value="inicio", game=game, player=maxPlayer)

