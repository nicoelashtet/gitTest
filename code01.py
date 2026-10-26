import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
rect_x =100
rect_y=100
hero_color = (244,67,54)
my_font = pygame.font.SysFont(None, 50)
speed =20
running = True

def draw_snake(x, y):

    body = [
        (x-60, y),
        (x-45, y),
        (x-30, y),
        (x-15, y),
        (x, y)
    ]

    for i, (bx, by) in enumerate(body):

        if i == len(body)-1:
            pygame.draw.circle(screen, (0,200,0), (bx, by), 12)
            pygame.draw.circle(screen, (0,0,0), (bx, by), 4)
        else:
            pygame.draw.circle(screen, (0,255,0), (bx, by), 12)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                speed =170
            hero_color =(227,217,27)
            if event.key == pygame.K_UP:
                hero_y -= speed
            if event.key == pygame.K_DOWN:
                hero_y +=speed
            if event.key == pygame.K_LEFT:
                hero_x -=speed
            if event.key == pygame.K_RIGHT:
                hero_x +=speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed =20
            hero_color = (255,0,0)
                
    screen.fill((209,27,227))
    draw_snake(hero_x, hero_y)
    pygame.draw.rect(screen,(217,234,211),(rect_x,rect_y,30,30))
    if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
        rect_x = random.randint(20,480)
        rect_y = random.randint(20,480)
        
    if(hero_x>500  or hero_x<0 or hero_y>500 or hero_y <0):
        msg =my_font.render("Game Over", True, (239,244,234))
        screen.blit(msg, (150, 200))
    pygame.display.update()
    
pygame.quit()
