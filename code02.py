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
direction = "RIGHT"
snake_body = []
snake_length = 5

x_change = 0
y_change = 0

clock = pygame.time.Clock()

def draw_snake(body):
    for i, (x, y) in enumerate(body):
        if i == len(body)-1:
            pygame.draw.circle(screen, (0,200,0), (int(x), int(y)), 12)
            pygame.draw.circle(screen, (0,0,0), (int(x), int(y)), 4)
        else:
            pygame.draw.circle(screen, (0,255,0), (int(x), int(y)), 12)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                speed =170
            hero_color =(227,217,27)
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -speed

            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = speed

            if event.key == pygame.K_LEFT:
                x_change = -speed
                y_change = 0

            if event.key == pygame.K_RIGHT:
                x_change = speed
                y_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed =20
            hero_color = (255,0,0)
    
    hero_x += x_change
    hero_y += y_change
    screen.fill((209,27,227))
    snake_body.append((hero_x, hero_y))

    if len(snake_body) > snake_length:
        snake_body.pop(0)

    draw_snake(snake_body)
    
    pygame.draw.rect(screen,(217,234,211),(rect_x,rect_y,30,30))
    if(abs(hero_x - rect_x)<30 and abs(hero_y-rect_y)<30):
        rect_x = random.randint(20,480)
        rect_y = random.randint(20,480)
        
    if(hero_x>500  or hero_x<0 or hero_y>500 or hero_y <0):
        msg =my_font.render("Game Over", True, (239,244,234))
        screen.blit(msg, (150, 200))
        
    clock.tick(10)
    pygame.display.update()
    

pygame.quit()

