#02
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
rect_x = 250
rect_y = 400
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_y -= 50
                rect_y += 50
            if event.key == pygame.K_DOWN:
                hero_y += 50
                rect_y -= 50
            if event.key == pygame.K_LEFT:
                hero_x -= 50
                rect_x += 50
            if event.key == pygame.K_RIGHT:
                hero_x += 50
                rect_x -= 50

    screen.fill((209,27,227))
    pygame.draw.circle(screen, (227,217,27),(hero_x,hero_y),30)
    #pygame.draw.rect(screen,(0,255,0),(rect_x,rect_y,20,20))

    if hero_x < 0 or hero_x > 500 or hero_y < 0 or hero_y > 500:  # ★ NEW
        font = pygame.font.SysFont(None, 80)                         # ★ NEW
        msg = font.render("GAME OVER", True, (255,255,255))          # ★ NEW
        screen.blit(msg, (100, 200))                                 # ★ NEW

    pygame.display.update()

pygame.quit()

#003

import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
speed = 10                          # ★ NEW
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:  # ★ NEW
                speed = 70                    # ★ NEW
            if event.key == pygame.K_UP:
                hero_y -= speed
            if event.key == pygame.K_DOWN:
                hero_y += speed
            if event.key == pygame.K_LEFT:
                hero_x -= speed
            if event.key == pygame.K_RIGHT:
                hero_x += speed
        if event.type == pygame.KEYUP:        # ★ NEW
            if event.key == pygame.K_LSHIFT:  # ★ NEW
                speed = 10                    # ★ NEW

    screen.fill((209,27,227))
    pygame.draw.circle(screen, (227,217,27),(hero_x,hero_y),30)
    pygame.display.update()

pygame.quit()

# 004
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
speed = 10
hero_color = (255, 255, 0)          # ★ NEW
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                speed = 30
            hero_color = (255, 0, 0)            # ★ NEW
            if event.key == pygame.K_UP:
                hero_y -= speed
            if event.key == pygame.K_DOWN:
                hero_y += speed
            if event.key == pygame.K_LEFT:
                hero_x -= speed
            if event.key == pygame.K_RIGHT:
                hero_x += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed = 10
            hero_color = (255, 255, 0)          # ★ NEW

    screen.fill((209,27,227))
    pygame.draw.circle(screen, hero_color, (hero_x,hero_y), 30)  # ★ NEW
    pygame.display.update()

pygame.quit()

#005
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
speed = 10
hero_color = (255, 255, 0)
rect_x = 100                        # ★ NEW
rect_y = 100                        # ★ NEW
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                speed = 30
            hero_color = (255, 0, 0)
            if event.key == pygame.K_UP:
                hero_y -= speed
            if event.key == pygame.K_DOWN:
                hero_y += speed
            if event.key == pygame.K_LEFT:
                hero_x -= speed
            if event.key == pygame.K_RIGHT:
                hero_x += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed = 10
            hero_color = (255, 255, 0)

    screen.fill((209,27,227))
    pygame.draw.circle(screen, hero_color, (hero_x,hero_y), 30)
    pygame.draw.rect(screen, (0,255,0), (rect_x,rect_y,30,30))    # ★ NEW

    if abs(hero_x - rect_x) < 30 and abs(hero_y - rect_y) < 30:  # ★ NEW
        rect_x = random.randint(30, 470)                                             # ★ NEW
        rect_y = random.randint(30, 470)                                             # ★ NEW

    pygame.display.update()

pygame.quit()
