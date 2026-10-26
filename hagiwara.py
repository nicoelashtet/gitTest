# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Move Hero")
# hero_x = 250
# hero_y = 250
# rect_x =100
# rect_y =100
# my_font = pygame.font.SysFont(None,50)
# speed = 50
# running = True
# pygame.mixer.init()
# # sound = pygame.mixer.Sound("voice.mp3")
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LSHIFT:
#                 speed =170
#             hero_color = (255,0,0)
#             if event.key == pygame.K_UP:
#                 hero_y -=speed
                
#             if event.key == pygame.K_DOWN:
#                 hero_y +=speed
                
#             if event.key == pygame.K_LEFT:
#                 hero_x -=speed
                
#             if event.key == pygame.K_RIGHT:
#                 hero_x +=speed
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LSHIFT:
#                 speed =20
#             hero_color = (255,0,0)
#     screen.fill((75,77,73))
#     pygame.draw.circle(screen,(106,163,0),(hero_x,hero_y),20)
#     pygame.draw.circle(screen,(0,0,0),(hero_x+6,hero_y-5),3)
#     pygame.draw.circle(screen,(0,0,0),(hero_x+6,hero_y+5),3)
#     pygame.draw.circle(screen,(0,120,0),(hero_x-18,hero_y),12)
#     pygame.draw.circle(screen,(0,120,0),(hero_x-32,hero_y),10)
#     pygame.draw.circle(screen,(0,120,0),(hero_x-44,hero_y),8)
#     pygame.draw.circle(screen,(0,120,0),(hero_x-54,hero_y),6)
#     pygame.draw.circle(screen,(0,120,0),(hero_x-62,hero_y),4)
#     pygame.draw.rect(screen,(109,145,45),(rect_x,rect_y,30,30),30)
#     if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
#         rect_x =random.randint(20,480)
#         rect_y =random.randint(20,480)
#         sound.play()

#     if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y <0):
#         msg =my_font.render("Game Over", True, (239,244,234))
#         screen.blit(msg,(150,200))
#     pygame.display.update()
    
# pygame.quit()

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move Hero")

hero_x = 250
hero_y = 250
rect_x = 100
rect_y = 100

my_font = pygame.font.SysFont(None, 50)

speed = 20          # Changed from 50 to 20
running = True

# ===== NEW: Create a list to store the snake body =====
snake = []

# ===== NEW: Create the initial snake body =====
for i in range(6):
    snake.append((hero_x - i * 30, hero_y))

while running:

    # ===== NEW: Check whether the hero moved =====
    moved = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LSHIFT:
                speed = 170
            if event.key == pygame.K_UP:
                hero_y -= speed
                moved = True          # NEW: Hero moved
            elif event.key == pygame.K_DOWN:
                hero_y += speed
                moved = True          # NEW: Hero moved
            elif event.key == pygame.K_LEFT:
                hero_x -= speed
                moved = True          # NEW: Hero moved
            elif event.key == pygame.K_RIGHT:
                hero_x += speed
                moved = True          # NEW: Hero moved
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed = 20

    # ===== NEW: Update the snake body =====
    if moved:
        snake.insert(0, (hero_x, hero_y))   # NEW: Add new head position
        snake.pop()                         # NEW: Remove the last body part

    screen.fill((209, 27, 227))
    # ===== NEW: Draw the snake =====
    for i, (x, y) in enumerate(snake):
        # ===== NEW: Draw the snake head =====
        if i == 0:
            pygame.draw.circle(screen, (0, 200, 0),(x, y),20)
            # NEW: White eyes
            pygame.draw.circle(screen,(255, 255, 255),(x + 6, y - 5),4)
            pygame.draw.circle(screen,(255, 255, 255),(x + 6, y + 5),4)

            # NEW: Black pupils
            pygame.draw.circle(screen,(0, 0, 0),(x + 6, y - 5),2)
            pygame.draw.circle(screen,(0, 0, 0),(x + 6, y + 5),2)

            # NEW: Red tongue
            pygame.draw.line(screen,(255, 0, 0),(x + 20, y),(x + 30, y - 4),2)

        # ===== NEW: Draw the snake body =====
        else:
            radius = max(4, 20 - i * 2)          # NEW: Make the body gradually smaller
            green = max(80, 200 - i * 20)        # NEW: Make the color darker

            pygame.draw.circle(screen,(0, green, 0),(x, y),radius)

    # Draw food
    pygame.draw.rect(screen,(217, 234, 19),(rect_x, rect_y, 30, 30),30)

    # Collision detection
    if abs(hero_x - rect_x) < 30 and abs(hero_y - rect_y) < 30:
        rect_x = random.randint(20, 480)
        rect_y = random.randint(20, 480)

    # Game Over
    if hero_x > 500 or hero_x < 0 or hero_y > 500 or hero_y < 0:
        msg = my_font.render("Game Over",True,(239, 244, 234))
        screen.blit(msg, (150, 200))
    pygame.display.update()
pygame.quit()