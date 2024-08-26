from Map.Map import TronMap
from AI.TronTree import TronTree
from AI.TronNode import TronNode
import os
import time
from copy import deepcopy

# Define constants
INVALID = 400
VALID = 200
PLAYER_DEAD = 202

# Game configuration
GAME_WIDTH = 20
GAME_HEIGHT = 20
NUM_PLAYERS = 2
MAX_PLAYER = 1  # Player 1 is Max, thus Player 2 is Min (duh)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_beautiful_map(game_map):
    clear_screen()
    print("+" + "-" * (game_map._width * 2 + 1) + "+")
    for row in game_map._map:
        print("|", end=" ")
        for cell in row:
            if cell == 0:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print("|")
    print("+" + "-" * (game_map._width * 2 + 1) + "+")


def move(game: TronMap, is_max_player: bool):
    treeAlphaBeta = TronTree(deepcopy(game), is_max_player)
    objective = treeAlphaBeta.alphaBeta(4, maxPlayer=is_max_player)
    player = (
        MAX_PLAYER if is_max_player else (3 - MAX_PLAYER)
    )  # 3 - MAX_PLAYER gives us the other player
    game.add_move(objective.state[player - 1][0], objective.state[player - 1][1])
    print(
        f"Decision {'Max' if is_max_player else 'Min'}:",
        objective.state[player - 1][0],
        ",",
        objective.state[player - 1][1],
    )


def player_move(game: TronMap, current_player: int):
    current_pos = game.get_player_position(current_player)
    print(f"You are Player {current_player}")
    print(f"Your current position is: {current_pos}")
    while True:
        move = input("Enter your move (up/down/left/right): ").lower()
        if move == "up":
            new_pos = (current_pos[0] - 1, current_pos[1])
        elif move == "down":
            new_pos = (current_pos[0] + 1, current_pos[1])
        elif move == "left":
            new_pos = (current_pos[0], current_pos[1] - 1)
        elif move == "right":
            new_pos = (current_pos[0], current_pos[1] + 1)
        else:
            print("Invalid input. Please enter up, down, left, or right.")
            continue

        status, message = game.add_move(new_pos[0], new_pos[1])
        if status == VALID:
            print(f"Move successful. New position: {new_pos}")
            break
        else:
            print(f"Invalid move: {message}. Try again.")


def play_game(player_vs_ai=True):
    game = TronMap(GAME_WIDTH, GAME_HEIGHT, NUM_PLAYERS)
    turns = [0, 0]

    while not game.game_finished():
        print_beautiful_map(game)
        current_player = game.get_current_player()
        is_max_player = current_player == MAX_PLAYER

        print(f"Player {current_player}'s turn")
        print(f"Player 1 position: {game.get_player_position(1)}")
        print(f"Player 2 position: {game.get_player_position(2)}")

        if player_vs_ai and current_player == 1:
            player_move(game, current_player)
        else:
            move(game, is_max_player)

        turns[current_player - 1] += 1
        # time.sleep(0.5)

    print_beautiful_map(game)
    print("Game Over!")

    # Determine the winner
    player1_alive = (
        game.check_player_dead(
            game.get_player_position(1)[0], game.get_player_position(1)[1]
        )
        == 0
    )
    player2_alive = (
        game.check_player_dead(
            game.get_player_position(2)[0], game.get_player_position(2)[1]
        )
        == 0
    )

    if player1_alive and not player2_alive:
        winner = "Player 1"
    elif player2_alive and not player1_alive:
        winner = "Player 2"
    else:
        winner = "Draw"

    print(f"Winner: {winner}")
    print("Final positions:", game.get_players_positions())
    print(f"Total turns: Player 1: {turns[0]}, Player 2: {turns[1]}")
    input("Press Enter to return to the main menu...")


def main_menu():
    while True:
        clear_screen()
        print("Welcome to Tron CLI Game!")
        print("1. Player vs AI")
        print("2. AI vs AI")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            play_game(player_vs_ai=True)
        elif choice == "2":
            play_game(player_vs_ai=False)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
