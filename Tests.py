from copy import deepcopy
from AI import TronNode, TronTree
from Map.Map import TronMap

def printChildrenRecursive(node, depth):
  for child in node.children:
    print("\t"*depth, child.state, ": Alpha:", child.alpha, "Beta:", child.beta, "Heuristic:", child.heuristic())
    if child.children:
      printChildrenRecursive(child, depth+1)

def originalTests():
  game = TronMap()
  print(game._num_players)
  print(game._current_player)
  game.print_map()
  print([game.get_player_position(1), game.get_player_position(2)])
  # Max
  treeAlphaBeta = TronTree(game, True)
  objective = treeAlphaBeta.alphaBeta(5, maxPlayer=treeAlphaBeta.root.player)
  print("Decision: ", objective.state)
  print("Children: ", end="")
  for child in objective.children:
    print(child.state, end=", ")
  print()

  game.add_move(objective.state[0][0], objective.state[0][1])

  index = 1
  printChildrenRecursive(treeAlphaBeta.root, 0)
  # Min
  #nodeInit=NodeTicTacToe(False,value="inicio",state=initState, operators= operators)
  #treeAlphaBeta= Tree(nodeInit,operators)
  #objective=treeAlphaBeta.alfaBeta(5, maxPlayer=False)

  # path=treeAlphaBeta.printPath(objective)
  # graph=treeAlphaBeta.draw(path.copy())
  # tree_image = Image(graph.create_png(), width=10000, height=10000)
  # display(tree_image)

def gameBetweenAI():
  nodes = []
  game = TronMap()
  print("Number of players:", game._num_players)
  game.print_map()
  print()

  currentPlayer = True
  while not game.game_finished():
    move(game, currentPlayer)
    game.print_map()
    print()

    currentPlayer = not currentPlayer

  print(game.get_players_positions())
  return game

def move(game: TronMap, player: bool):
  treeAlphaBeta = TronTree(deepcopy(game), player)
  objective = treeAlphaBeta.alphaBeta(5, maxPlayer=treeAlphaBeta.root.player)
  if player:
    game.add_move(objective.state[0][0], objective.state[0][1])
    print("Decision Max:", objective.state[0][0], ",", objective.state[0][1])
  else:
    game.add_move(objective.state[1][0], objective.state[1][1])
    print("Decision Min:", objective.state[1][0], ",", objective.state[1][1])


if __name__ == "__main__":
  gameBetweenAI()
  