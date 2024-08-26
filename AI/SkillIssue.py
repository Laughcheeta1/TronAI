from . import DifficultyConstants
from . import TronTree


def recommend(game, maxPlayer, difficulty) -> list[int, int]:
    """
    Recommends a move for the player based on the difficulty level.

    Parameters:
    - game: The game object to be used for the tree.
    - maxPlayer: Boolean indicating if the player is Max (True) or Min (False).
    - difficulty: The difficulty level of the AI.

    Returns: The recommended move.
    """
    # Get the recommended move depending on the difficulty level
    if str.lower(difficulty) == "hard":
        tree = TronTree(game, maxPlayer, nodeReachableSpaces=DifficultyConstants.HARD[1])
        move = tree.alphaBeta(DifficultyConstants.HARD[0], maxPlayer)
    elif str.lower(difficulty) == "medium":
        tree = TronTree(game, maxPlayer, nodeReachableSpaces=DifficultyConstants.MEDIUM[1])
        move = tree.alphaBeta(DifficultyConstants.MEDIUM[0], maxPlayer)
    else:
        if str.lower(difficulty) != "easy":
            print("Invalid difficulty level. Using easy level by default.")
        tree = TronTree(game, maxPlayer, nodeReachableSpaces=DifficultyConstants.EASY[1])
        move = tree.alphaBeta(DifficultyConstants.EASY[0], maxPlayer)

    return move.state[0] if maxPlayer else move.state[1]
