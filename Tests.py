from Tree import Tree
from Testing import NodeTicTacToe


if __name__ == "__main__":

  initState=[['X',' ',' '],
            [' ','O','X'],
            [' ','O',' ']]


  operators=[(i,j) for i,f in enumerate(initState) for j,c in enumerate(f)]


  # Max
  nodeInit=NodeTicTacToe(True,value="inicio",state=initState, operators= operators)
  treeAlphaBeta= Tree(nodeInit,operators)
  objective=treeAlphaBeta.alfaBeta(5, maxPlayer=True)

  # Min
  #nodeInit=NodeTicTacToe(False,value="inicio",state=initState, operators= operators)
  #treeAlphaBeta= Tree(nodeInit,operators)
  #objective=treeAlphaBeta.alfaBeta(5, maxPlayer=False)

  path=treeAlphaBeta.printPath(objective)
  # graph=treeAlphaBeta.draw(path.copy())
  # tree_image = Image(graph.create_png(), width=10000, height=10000)
  # display(tree_image)
