import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250

fences = []   # ← added: save fence positions

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
            elif event.key == pygame.K_SPACE:              # ← added
                fences.append((hero_x, hero_y))            # ← added

    screen.fill((245,237,243))

    # Draw all fences
    for fence_x, fence_y in fences:                         # ← added
        pygame.draw.rect(screen, (19, 232, 45), (fence_x - 25, fence_y - 25, 50, 50), 30)  # ← added

    # Hero
    pygame.draw.circle(screen,(245,10,200), (hero_x, hero_y), 20)
    pygame.display.update()
pygame.quit()