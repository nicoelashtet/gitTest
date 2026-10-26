# 1. Create a font for the score

# Add this after:


score_font = pygame.font.SysFont(None, 30)   # NEW: Font for the score
# 2. Create a score variable

# Add this after:

# game_speed = 10

# Add:

score = 0      # NEW: Starting score

# So it becomes:

speed = 20
game_speed = 10
score = 0      # NEW
running = True
# 3. Increase the score when the snake eats food

# Inside your collision detection, add:

# score += 1      # NEW: Increase the score

# So it becomes:

# Check whether the snake ate the food
if abs(hero_x - rect_x) < 30 and abs(hero_y - rect_y) < 30:

    rect_x = random.randint(20, 480)
    rect_y = random.randint(20, 480)

    game_speed += 2
    score += 1          # NEW: Increase the score

else:
    snake.pop()
# 4. Show the score

# Just before:

pygame.display.update()
# Add:

# NEW: Create the score message
score_msg = score_font.render("Score: " + str(score), True, (255,255,255))

# NEW: Display the score
screen.blit(score_msg, (10,10))

#So the end of your program becomes:

# NEW: Create the score message
score_msg = score_font.render("Score: " + str(score), True, (255,255,255))

# NEW: Display the score
screen.blit(score_msg, (10,10))

pygame.display.update()
clock.tick(game_speed)