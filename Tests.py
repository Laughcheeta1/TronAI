from AI import TronNode, TronTree
from Map.Map import TronMap

if __name__ == "__main__":

  game = TronMap()
  print(game._num_players)
  print(game._current_player)
  game.print_map()
  print([game.get_player_position(1), game.get_player_position(2)])
  # Max
  treeAlphaBeta = TronTree(game, True, True)
  objective = treeAlphaBeta.alphaBeta(8, maxPlayer=treeAlphaBeta.root.player)
  print(objective.state)

  game.add_move(objective.state[0][0], objective.state[0][1])

  print(game.game_finished())
  node = objective
  index = 1
  while(node.children):
    node = node.children[0]
    print(index, ": ", node.state)
    index += 1
  # Min
  #nodeInit=NodeTicTacToe(False,value="inicio",state=initState, operators= operators)
  #treeAlphaBeta= Tree(nodeInit,operators)
  #objective=treeAlphaBeta.alfaBeta(5, maxPlayer=False)

  # path=treeAlphaBeta.printPath(objective)
  # graph=treeAlphaBeta.draw(path.copy())
  # tree_image = Image(graph.create_png(), width=10000, height=10000)
  # display(tree_image)
