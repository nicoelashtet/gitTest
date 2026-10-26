import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ball Game")
bar_x =200
ball_y =0
ball_speed =6

ball_x = random.randint(10, 490)
score =0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bar_x -=5
    if keys[pygame.K_RIGHT]:
            bar_x +=5
    ball_y += ball_speed
    if ball_y > 500:
         ball_y =0
         ball_x = random.randint(10, 490)

    if ball_y >= 450 and ball_y <=465:
         if ball_x >= bar_x and ball_x <= bar_x +100:
              score +=1
              ball_y =0
              ball_x  =random.randint(10,490)
         

    screen.fill((0, 0, 0))

    # バー
    pygame.draw.rect(screen, (255, 255, 255), (bar_x, 460, 100, 15))

    # ボール
    pygame.draw.circle(screen, (255, 200, 0), (ball_x, ball_y), 10)
    text = font.render("Score" +str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()