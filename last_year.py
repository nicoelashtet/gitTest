import pygame, random
pygame.init()

# --- Setup & Colors ---
W, H = 800, 600
dis = pygame.display.set_mode((W, H))
pygame.display.set_caption('ヘビゲーム（Week4: 完成＋スピードUP）')
white, black = (255,255,255), (0,0,0)
red, blue = (255,0,0), (0,0,255)
green, green_01 = (0,200,0), (0,255,0)

snake_block = 10
BASE_SPEED, SPEED_MAX = 12, 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

def spawn_food():
    fx = round(random.randrange(0, W - snake_block) / 10)*10
    fy = round(random.randrange(0, H - snake_block) / 10)*10
    return fx, fy

def draw_snake(body):
    for i, (x, y) in enumerate(body):
        if i == len(body)-1:
            pygame.draw.circle(dis, green_01, (int(x), int(y)), 12)
            pygame.draw.circle(dis, black, (int(x), int(y)), 4)
        else:
            pygame.draw.circle(dis, green, (int(x), int(y)), 12)

def draw_hud(score, speed):
    dis.blit(font.render(f"Score: {score}", True, black), (10, 10))
    dis.blit(font.render(f"Speed: {int(speed)}", True, black), (10, 36))

def game_loop():
    x1, y1 = W//2, H//2
    x1_change = y1_change = 0
    snake_body, snake_length = [], 4
    foodx, foody = spawn_food()
    score, speed = 0, BASE_SPEED
    game_over, game_close = False, False

    while not game_over:
        # ----- Game Over Screen -----
        while game_close:
            dis.fill(white); draw_hud(score, speed)
            msg = "Game Over!  C: Play Again / Q: Quit"
            dis.blit(font.render(msg, True, red), (W//2-220, H//2-10))
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == pygame.QUIT: return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q: return
                    if e.key == pygame.K_c: return game_loop()

        # ----- Events -----
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:  x1_change, y1_change = -snake_block, 0
                if e.key == pygame.K_RIGHT: x1_change, y1_change =  snake_block, 0
                if e.key == pygame.K_UP:    y1_change, x1_change = -snake_block, 0
                if e.key == pygame.K_DOWN:  y1_change, x1_change =  snake_block, 0

        # ----- Update -----
        x1 += x1_change; y1 += y1_change
        if x1 < 0 or x1 >= W or y1 < 0 or y1 >= H: game_close = True

        dis.fill(white); draw_hud(score, speed)
        pygame.draw.rect(dis, blue, (foodx, foody, snake_block, snake_block))

        snake_body.append((x1, y1))
        if len(snake_body) > snake_length: snake_body.pop(0)
        draw_snake(snake_body)

        pygame.display.update()

        # Eat → grow & speed-up
        if x1 == foodx and y1 == foody:
            snake_length += 1; score += 1
            speed = min(BASE_SPEED + score//2, SPEED_MAX)  # 段階的UP（短くて分かりやすい）
            foodx, foody = spawn_food()

        clock.tick(int(speed))

game_loop()
pygame.quit(); quit()
