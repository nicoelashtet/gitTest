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
# sound = pygame.mixer.Sound("voice_01.wav")

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
#     screen.fill((209,27,227))
#     # 蛇作る
#     pygame.draw.circle(screen,(160,0,250),(hero_x+59,hero_y+43),11)
#     pygame.draw.circle(screen,(0,40,250),(hero_x+53,hero_y+39),14)
#     pygame.draw.circle(screen,(0,250,200),(hero_x+45,hero_y+35),16)
#     pygame.draw.circle(screen,(0,250,0),(hero_x+36,hero_y+30),20)
#     pygame.draw.circle(screen,(250,250,0),(hero_x+25,hero_y+25),23)
#     pygame.draw.circle(screen,(250,120,0),(hero_x+13,hero_y+13),26)
#     pygame.draw.circle(screen,(255,0,0),(hero_x,hero_y),30)
#     pygame.draw.circle(screen,(255,255,255),(hero_x+20,hero_y-19),6)
#     pygame.draw.circle(screen,(255,255,255),(hero_x-19,hero_y-19),6)
#     pygame.draw.circle(screen,(0,0,0),(hero_x-18,hero_y-18),3)
#     pygame.draw.circle(screen,(0,0,0),(hero_x+18,hero_y-18),3)
#     pygame.draw.rect(screen,(0,0,0),(hero_x-12,hero_y+10,25,2))
#     if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
#         rect_x =random.randint(20,480)
#         rect_y =random.randint(20,480)
#         sound.play()
        

#     if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y <0):
#         msg =my_font.render("Game Over", True, (239,244,234))
#         screen.blit(msg,(150,200))
#     pygame.display.update()
    
# pygame.quit()


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

# speed = 20          # NEW (changed from 50)
# running = True

# pygame.mixer.init()
# sound = pygame.mixer.Sound("voice_01.wav")

# hero_color = (255,0,0)

# # ===========================
# # NEW Create snake body list
# # ===========================
# snake = []                                  # NEW
# for i in range(7):                          # NEW
#     snake.append((hero_x + i*20, hero_y))   # NEW


# while running:

#     moved = False                           # NEW

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             pygame.quit()                   # NEW
#             quit()                          # NEW

#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_LSHIFT:
#                 speed =170

#             if event.key == pygame.K_UP:
#                 hero_y -=speed
#                 moved = True                # NEW

#             if event.key == pygame.K_DOWN:
#                 hero_y +=speed
#                 moved = True                # NEW

#             if event.key == pygame.K_LEFT:
#                 hero_x -=speed
#                 moved = True                # NEW

#             if event.key == pygame.K_RIGHT:
#                 hero_x +=speed
#                 moved = True                # NEW

#         if event.type == pygame.KEYUP:

#             if event.key == pygame.K_LSHIFT:
#                 speed =20

#     # ===========================
#     # NEW Update snake position
#     # ===========================
#     if moved:                               # NEW
#         snake.insert(0,(hero_x,hero_y))     # NEW
#         snake.pop()                         # NEW

#     screen.fill((209,27,227))


#     # ===========================
#     # NEW Draw flexible snake
#     # ===========================
#     pygame.draw.circle(screen,(160,0,250),snake[6],11)      # NEW
#     pygame.draw.circle(screen,(0,40,250),snake[5],14)       # NEW
#     pygame.draw.circle(screen,(0,250,200),snake[4],16)      # NEW
#     pygame.draw.circle(screen,(0,250,0),snake[3],20)        # NEW
#     pygame.draw.circle(screen,(250,250,0),snake[2],23)      # NEW
#     pygame.draw.circle(screen,(250,120,0),snake[1],26)      # NEW

#     head_x = snake[0][0]                                    # NEW
#     head_y = snake[0][1]                                    # NEW

#     pygame.draw.circle(screen,hero_color,(head_x,head_y),30)   # NEW

#     pygame.draw.circle(screen,(255,255,255),(head_x+20,head_y-19),6)   # NEW
#     pygame.draw.circle(screen,(255,255,255),(head_x-19,head_y-19),6)   # NEW

#     pygame.draw.circle(screen,(0,0,0),(head_x-18,head_y-18),3)          # NEW
#     pygame.draw.circle(screen,(0,0,0),(head_x+18,head_y-18),3)          # NEW

#     pygame.draw.rect(screen,(0,0,0),(head_x-12,head_y+10,25,2))         # NEW


#     pygame.draw.rect(screen,(217,234,19),(rect_x,rect_y,30,30),30)

#     if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):

#         rect_x =random.randint(20,480)
#         rect_y =random.randint(20,480)

#         sound.play()


#     if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y <0):

#         msg =my_font.render("Game Over", True, (239,244,234))
#         screen.blit(msg,(150,200))

#     pygame.display.update()

# pygame.quit()



#my practise

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

hero_color =(255,0,0)

snake =[]

for i in range(7):
    snake.append((hero_x + i*20, hero_y))

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
        snake.insert(0, (hero_x, hero_y))
        snake.pop()

    screen.fill((209,27,227))
    # 蛇作る
    pygame.draw.circle(screen,(160,0,250),snake[6],11)
    pygame.draw.circle(screen,(0,40,250),snake[5],14)
    pygame.draw.circle(screen,(0,250,200),snake[4],16)
    pygame.draw.circle(screen,(0,250,0),snake[3],20)
    pygame.draw.circle(screen,(250,250,0),snake[2],23)
    pygame.draw.circle(screen,(250,120,0),snake[1],26)

    head_x=snake[0][0]
    head_y = snake[0][1]

    pygame.draw.circle(screen,hero_color,(head_x,head_y),30)
    pygame.draw.circle(screen,(255,255,255),(head_x+20,head_y-19),6)
    pygame.draw.circle(screen,(255,255,255),(head_x-19,head_y-19),6)

    pygame.draw.circle(screen,(0,0,0),(head_x-18,head_y-18),3)
    pygame.draw.circle(screen,(0,0,0),(head_x+18,head_y-18),3)

    pygame.draw.rect(screen,(0,0,0),(head_x-12,head_y+10,25,2))

    pygame.draw.rect(screen,(217,234,19),(rect_x, rect_y, 30, 30), 30) #food


    if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
        rect_x =random.randint(20,480)
        rect_y =random.randint(20,480)
        sound.play()
        

    if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y <0):
        msg =my_font.render("Game Over", True, (239,244,234))
        screen.blit(msg,(150,200))
    pygame.display.update()
    
pygame.quit()