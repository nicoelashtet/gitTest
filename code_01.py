import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
rect_x =100
rect_y =100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_y -= 50
            elif event.key == pygame.K_DOWN:
                hero_y += 50
            elif event.key == pygame.K_LEFT:
                hero_x -= 50
            elif event.key == pygame.K_RIGHT:
                hero_x += 50
    screen.fill((245,237,243))
    pygame.draw.circle(screen, (245,10,200), (hero_x, hero_y), 20)
    pygame.draw.rect(screen,(217,234,211),(rect_x,rect_y,30,30))
    pygame.display.update()
pygame.quit()

print("hello git hub")
print("This is Version 2")