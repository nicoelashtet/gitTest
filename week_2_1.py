import pygame
import sys
import random

pygame.init()

WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Coin")

clock = pygame.time.Clock()
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
BLUE = (0, 120, 220)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
RED = (200, 30, 30)

# Player
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 20
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - 50
PLAYER_SPEED = 6

# Coin
COIN_SIZE = 20
coin_x = random.randint(0, WIDTH - COIN_SIZE)
coin_y = 0
COIN_SPEED = 4

# Score / lives / game state (NEW this week)
score = 0
lives = 3
game_over = False

font = pygame.font.SysFont("arial", 32, bold=True)
game_over_font = pygame.font.SysFont("arial", 48, bold=True)


def reset_game():
    global player_x, coin_x, coin_y, score, lives, game_over
    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    coin_x = random.randint(0, WIDTH - COIN_SIZE)
    coin_y = 0
    score = 0
    lives = 3
    game_over = False


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

    # ---------------------------------------------
    # Everything below only runs while the game is
    # actually being played. Once game_over is True,
    # this whole block is skipped every frame.
    # ---------------------------------------------
    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        if player_x < 0:
            player_x = 0
        if player_x > WIDTH - PLAYER_WIDTH:
            player_x = WIDTH - PLAYER_WIDTH

        coin_y += COIN_SPEED

        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        coin_rect = pygame.Rect(coin_x, coin_y, COIN_SIZE, COIN_SIZE)

        if player_rect.colliderect(coin_rect):
            score += 1
            coin_y = 0
            coin_x = random.randint(0, WIDTH - COIN_SIZE)

        if coin_y > HEIGHT:
            coin_y = 0
            coin_x = random.randint(0, WIDTH - COIN_SIZE)
            lives -= 1
            if lives <= 0:
                game_over = True

    # Drawing always happens, even when game_over is True,
    # so the final screen stays visible.
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, GOLD, (coin_x, coin_y, COIN_SIZE, COIN_SIZE))

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(lives_text, (10, 50))

    if game_over:
        msg = game_over_font.render("GAME OVER", True, RED)
        restart_msg = font.render("Press R to restart", True, BLACK)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(restart_msg, (WIDTH // 2 - restart_msg.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()

pygame.quit()
sys.exit()