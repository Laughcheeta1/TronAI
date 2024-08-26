import sys
from copy import deepcopy

import pygame

from AI import recommend
from Map.Map import TronMap

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 15
GAME_WIDTH = 35
GAME_HEIGHT = 35
NUM_PLAYERS = 2
MAX_PLAYER = 1

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tron")

# Font
font = pygame.font.Font(None, 36)


def draw_grid(game):
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if game._map[y][x] == 1:
                pygame.draw.rect(screen, BLUE, rect)
            elif game._map[y][x] == 2:
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)


def draw_info(turns):
    # Draw the info section on the right
    info_rect = pygame.Rect(SCREEN_WIDTH * 0.65, 0, SCREEN_WIDTH * 0.35, SCREEN_HEIGHT)
    pygame.draw.rect(screen, BLACK, info_rect)

    # Display turn information
    turn_text = font.render(f"P1: {turns[0]}, P2: {turns[1]}", True, WHITE)
    screen.blit(turn_text, (SCREEN_WIDTH * 0.7, 20))


def draw_title(mode):
    # Draw the title rectangle at the bottom
    title_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    pygame.draw.rect(screen, WHITE, title_rect)

    # Set the title based on the game mode
    title_text = "TRON: Human vs AI" if mode == "human_vs_ai" else "TRON: AI vs AI"
    title_surface = font.render(title_text, True, BLACK)
    text_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 25))
    screen.blit(title_surface, text_rect)


def move(game: TronMap, is_max_player: bool, difficulty: str):
    recommended_move = recommend(deepcopy(game), is_max_player, difficulty)
    game.add_move(recommended_move[0], recommended_move[1])


def select_difficulty():
    while True:
        screen.fill(BLACK)
        title = font.render("Select Difficulty", True, WHITE)
        option1 = font.render("1. Easy", True, WHITE)
        option2 = font.render("2. Medium", True, WHITE)
        option3 = font.render("3. Hard", True, WHITE)
        option4 = font.render("4. Back to Main Menu", True, WHITE)

        screen.blit(title, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))
        screen.blit(option1, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        screen.blit(option2, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
        screen.blit(option3, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100))
        screen.blit(option4, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_game(player_vs_ai=True, difficulty="easy")
                elif event.key == pygame.K_2:
                    play_game(player_vs_ai=True, difficulty="medium")
                elif event.key == pygame.K_3:
                    play_game(player_vs_ai=True, difficulty="hard")
                elif event.key == pygame.K_4:
                    main_menu()


def play_game(player_vs_ai=True, difficulty="hard"):
    game = TronMap(GAME_WIDTH, GAME_HEIGHT, NUM_PLAYERS)
    turns = [0, 0]
    clock = pygame.time.Clock()
    last_pos = None

    # Set the game mode for the title
    mode = "human_vs_ai" if player_vs_ai else "ai_vs_ai"

    while not game.game_finished():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw the game grid on the left
        draw_grid(game)

        # Draw the info section on the right
        draw_info(turns)

        current_player = game.get_current_player()
        is_max_player = current_player == MAX_PLAYER

        if player_vs_ai and current_player == 1:
            keys = pygame.key.get_pressed()
            current_pos = game.get_player_position(current_player)
            new_pos = current_pos

            if keys[pygame.K_LEFT]:
                new_pos = (current_pos[0] - 1, current_pos[1])
            elif keys[pygame.K_RIGHT]:
                new_pos = (current_pos[0] + 1, current_pos[1])
            elif keys[pygame.K_UP]:
                new_pos = (current_pos[0], current_pos[1] - 1)
            elif keys[pygame.K_DOWN]:
                new_pos = (current_pos[0], current_pos[1] + 1)

            if new_pos != current_pos and new_pos != last_pos:
                status, _ = game.add_move(new_pos[0], new_pos[1])
                if status == 200:  # VALID
                    turns[current_player - 1] += 1
                    last_pos = current_pos

        else:
            move(game, is_max_player, difficulty)
            turns[current_player - 1] += 1

        # Draw the title at the bottom
        draw_title(mode)

        pygame.display.flip()
        clock.tick(30)  # Limit to 5 FPS for visibility

    # Game over
    screen.fill(BLACK)
    draw_grid(game)

    # Determine the winner
    player1_alive = (game.check_player_dead(game.get_player_position(1)[0], game.get_player_position(1)[1]) == 0)
    player2_alive = (game.check_player_dead(game.get_player_position(2)[0], game.get_player_position(2)[1]) == 0)

    if player1_alive and not player2_alive:
        winner = "Player 1"
    elif player2_alive and not player1_alive:
        winner = "Player 2"
    else:
        winner = "Draw"

    # Draw a black rectangle behind the game over text
    game_over_text = font.render("Game Over! (0 to go to Main Menu)", True, WHITE)
    winner_text = font.render(f"Winner: {winner}", True, WHITE)
    turns_text = font.render(f"Total turns - P1: {turns[0]}, P2: {turns[1]}", True, WHITE)

    # Calculate text positions
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    turns_rect = turns_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    # Draw rectangles behind the text
    pygame.draw.rect(screen, BLACK, game_over_rect.inflate(20, 10))  # Inflate for padding
    pygame.draw.rect(screen, BLACK, winner_rect.inflate(20, 10))
    pygame.draw.rect(screen, BLACK, turns_rect.inflate(20, 10))

    # Blit the text
    screen.blit(game_over_text, game_over_rect)
    screen.blit(winner_text, winner_rect)
    screen.blit(turns_text, turns_rect)

    pygame.display.flip()

    # Wait for user to press 0 to return to the main menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:  # Press 0 to return to the main menu
                    waiting = False

    main_menu()  # Return to the main menu


def main_menu():
    while True:
        screen.fill(BLACK)
        title = font.render("Tron", True, WHITE)
        option1 = font.render("1. Player vs AI", True, WHITE)
        option2 = font.render("2. AI vs AI", True, WHITE)
        option3 = font.render("3. Quit", True, WHITE)

        screen.blit(title, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100))
        screen.blit(option1, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        screen.blit(option2, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
        screen.blit(option3, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    select_difficulty()
                elif event.key == pygame.K_2:
                    play_game(player_vs_ai=False)  # AI vs AI mode
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main_menu()
