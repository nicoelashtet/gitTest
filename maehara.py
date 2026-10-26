import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move Hero")

hero_x = 250
hero_y = 250

rect_y = 100
rect_x = 100

hero_color = (244,67,53)

my_font = pygame.font.SysFont(None, 50)

speed = 20
running = True

snake = []                              # NEW


for i in range(6):                      # NEW
    snake.append((hero_x - i * 20, hero_y))   # NEW

while running:

    moved = False                       # NEW

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LSHIFT:
                speed = 70

            hero_color = (227,217,27)

            if event.key == pygame.K_UP:
                hero_y -= speed
                moved = True            # NEW

            elif event.key == pygame.K_DOWN:
                hero_y += speed
                moved = True            # NEW

            elif event.key == pygame.K_LEFT:
                hero_x -= speed
                moved = True            # NEW

            elif event.key == pygame.K_RIGHT:
                hero_x += speed
                moved = True            # NEW

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LSHIFT:
                speed = 20

            hero_color = (0,88,45)

    
    if moved:                           # NEW
        snake.insert(0, (hero_x, hero_y))   # NEW
        snake.pop()                     # NEW

    screen.fill((50,100,255))    
    for i, (x, y) in enumerate(snake):      # NEW
        pygame.draw.circle(screen, hero_color, (x, y), 15)
        if i == 0:
            pygame.draw.circle(screen, (255,255,255), (x+5, y-5), 3)
            pygame.draw.circle(screen, (255,255,255), (x+5, y+5), 3)

            pygame.draw.circle(screen, (0,0,0), (x+5, y-5), 1)
            pygame.draw.circle(screen, (0,0,0), (x+5, y+5), 1)

            pygame.draw.polygon(
                screen,
                (255,0,0),
                [
                    (x+15, y),
                    (x+28, y-5),
                    (x+28, y+5)
                ]
            )
    pygame.draw.rect(screen, (217,27,227), (rect_x, rect_y, 30, 30))
    if abs(hero_x - rect_x) < 30 and abs(hero_y - rect_y) < 30:

        rect_x = random.randint(20,480)
        rect_y = random.randint(20,480)

    if hero_x > 500 or hero_x < 0 or hero_y > 500 or hero_y < 0:

        msg = my_font.render("Game Over", True, (255,0,0))
        screen.blit(msg, (150,200))
    pygame.display.update()
pygame.quit()