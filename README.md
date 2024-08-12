# About the project
This is a project meant to be part of the Artificial Intelligence class Midterm exam.

It is a Alpha-Beta prunning implementation in the game Tron.

## About the Algorithm
Alpha-Beta prunning is an algorithm for playing games escentially, it is a more advanced version of the Mini-max algorithm, since Alpha-Beta prunning is a more efficient way to search for an optimal play.

This algorithm is meant to be used as an AI against another player (be it human or otherwise), and it will (depending on computational power) always find the best move to make.

### How it works
At a high level the Mini-Max algorithm (father of Alpha-Beta) works by traversing the "whole" tree structure of the game, that is searching all posible states of a game, and searching for a path that results in the best possible result, and therefore the AI picks the actions that will lead to it.

Alpha-Beta prunning does something similar, but optimizes the inner workings of the Mini-Max in such a way that it reduces the ammount of possible games states that is has to consider, for getting a best case scenario.

### About the restrictions of Alpha-Beta prunning
This restrictions apply for both Mini-Max and Alpha beta prunning, but specially to the first one, that is, the larger the game, the more ammount of possibilities that need to be computed, as an example, there are more possible chess games than atoms in the universe, so to be able to traverse all this possibilities, with current technologies it would take more time than the life of the universe; that is to say, in some games, due to technical limitations, the algorithm has to be capped to a certain limit, to be able to give at least an approximate answer.
