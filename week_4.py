import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
rect_x =100
rect_y =100
my_font = pygame.font.SysFont(None,50)
speed = 20
running = True
pygame.mixer.init()
sound = pygame.mixer.Sound("voice_01.wav")
snake =[]
for i in range(6):
    snake.append((hero_x -i*20, hero_y))

while running:
    moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                speed =170
            hero_color = (255,0,0)
            if event.key == pygame.K_UP:
                hero_y -=speed
                moved = True
                
            if event.key == pygame.K_DOWN:
                hero_y +=speed
                moved = True
                
            if event.key == pygame.K_LEFT:
                hero_x -=speed
                moved = True
                
            if event.key == pygame.K_RIGHT:
                hero_x +=speed
                moved = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed =20
            hero_color = (255,0,0)

    if moved:
        snake.insert(0, (hero_x,hero_y))
        snake.pop()
    screen.fill((209,27,227))

    for i, (x,y) in enumerate(snake):
        if i==0:
            pygame.draw.circle(screen,(0,200,0),(hero_x,hero_y),20)
            pygame.draw.circle(screen,(255,255,255),(hero_x+6,hero_y-5),4)
            pygame.draw.circle(screen,(255,255,255),(hero_x+6,hero_y+5),4)

            pygame.draw.circle(screen,(0,0,0),(hero_x+6,hero_y-5),2)
            pygame.draw.circle(screen,(0,0,0),(hero_x+6,hero_y+5),2)

            pygame.draw.line(screen,(255,0,0),(hero_x+20,hero_y),(hero_x+30,hero_y-4),2)
        else:
            radius = max(4,20-i*2)
            green = max(80, 200-i*20)
            pygame.draw.circle(screen, (0, green, 0), (x,y), radius)    
    
    
    pygame.draw.rect(screen,(217,234,19),(rect_x,rect_y,30,30),30)
    if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
        rect_x =random.randint(20,480)
        rect_y =random.randint(20,480)
        sound.play()
        # snake.append(snake[-1])
        

    if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y <0):
        msg =my_font.render("Game Over", True, (239,244,234))
        screen.blit(msg,(150,200))
    pygame.display.update()
    
pygame.quit()

# import pygame
# import random

# pygame.init()

# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Move Hero")

# hero_x = 250
# hero_y = 250

# rect_x = 100
# rect_y = 100

# my_font = pygame.font.SysFont(None,50)

# speed = 20
# running = True

# pygame.mixer.init()
# sound = pygame.mixer.Sound("voice_01.wav")

# # Store snake body positions
# snake = []

# # Initial snake (6 body parts)
# for i in range(6):
#     snake.append((hero_x - i*30, hero_y))

# while running:

#     moved = False

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_LSHIFT:
#                 speed = 170

#             if event.key == pygame.K_UP:
#                 hero_y -= speed
#                 moved = True

#             if event.key == pygame.K_DOWN:
#                 hero_y += speed
#                 moved = True

#             if event.key == pygame.K_LEFT:
#                 hero_x -= speed
#                 moved = True

#             if event.key == pygame.K_RIGHT:
#                 hero_x += speed
#                 moved = True

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LSHIFT:
#                 speed = 20

#     # Move snake only when hero moves
#     if moved:
#         snake.insert(0,(hero_x,hero_y))
#         snake.pop()

#     screen.fill((209,27,227))

#     # Draw snake
#     for i,(x,y) in enumerate(snake):

#         if i == 0:
#             # Head
#             pygame.draw.circle(screen,(0,200,0),(x,y),20)

#             pygame.draw.circle(screen,(255,255,255),(x+6,y-5),4)
#             pygame.draw.circle(screen,(255,255,255),(x+6,y+5),4)

#             pygame.draw.circle(screen,(0,0,0),(x+6,y-5),2)
#             pygame.draw.circle(screen,(0,0,0),(x+6,y+5),2)

#             pygame.draw.line(screen,(255,0,0),(x+20,y),(x+30,y-4),2)

#         else:
#             radius = max(4,20-i*2)
#             green = max(80,200-i*20)

#             pygame.draw.circle(screen,(0,green,0),(x,y),radius)

#     pygame.draw.rect(screen,(217,234,19),(rect_x,rect_y,30,30))

#     # Eat food
#     if abs(hero_x-rect_x)<30 and abs(hero_y-rect_y)<30:

#         rect_x = random.randint(20,470)
#         rect_y = random.randint(20,470)

#         sound.play()

#         # Grow snake
#         snake.append(snake[-1])

#     # Game Over
#     if hero_x>500 or hero_x<0 or hero_y>500 or hero_y<0:

#         msg = my_font.render("Game Over",True,(239,244,234))
#         screen.blit(msg,(150,200))

#     pygame.display.update()

# pygame.quit()