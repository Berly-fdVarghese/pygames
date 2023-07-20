import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders - Levels and Mouse Control")

# Player properties
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Enemy properties
enemy_width = 50
enemy_height = 50
enemies = []
enemy_speed = 2

# Bullet properties
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Score and level
score = 0
level = 1
font = pygame.font.SysFont(None, 30)

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

def generate_enemies(num_enemies):
    global enemies
    enemies = []
    for _ in range(num_enemies):
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = random.randint(50, 200)
        enemies.append((enemy_x, enemy_y))

def draw_enemies():
    for enemy_x, enemy_y in enemies:
        pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_width, enemy_height))

def fire_bullet(x, y):
    bullets.append((x, y))

def move_bullets():
    for i in range(len(bullets)):
        x, y = bullets[i]
        y -= bullet_speed
        bullets[i] = (x, y)

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    return distance < 27  # Adjust this value for better accuracy

def draw_score():
    score_display = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_display, (10, 10))

def game_over():
    game_over_font = pygame.font.SysFont(None, 50)
    game_over_text = game_over_font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Initialize the first level
generate_enemies(6)

# Clock object to control FPS
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player controls using the mouse
        if event.type == pygame.MOUSEMOTION:
            player_x, player_y = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_x = player_x + player_width // 2 - bullet_width // 2
            bullet_y = player_y
            fire_bullet(bullet_x, bullet_y)

        # Player controls using keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                fire_bullet(bullet_x, bullet_y)

    screen.fill((0, 0, 0))

    # Enemy movement
    for i in range(len(enemies)):
        enemy_x, enemy_y = enemies[i]
        enemy_x += enemy_speed
        enemies[i] = (enemy_x, enemy_y)
        if enemy_x <= 0 or enemy_x >= SCREEN_WIDTH - enemy_width:
            enemy_speed *= -1
            enemy_y += 20
            enemies[i] = (enemy_x, enemy_y)

    # Bullet movement
    move_bullets()

    # Check for collision with enemies
    for enemy_x, enemy_y in enemies:
        for bullet_x, bullet_y in bullets:
            if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
                bullets.remove((bullet_x, bullet_y))
                enemies.remove((enemy_x, enemy_y))
                score += 10

    # If all enemies are destroyed, go to the next level
    if not enemies:
        level += 1
        if level <= 5:
            generate_enemies(6 + level * 2)  # Increase the number of enemies with each level
            bullets.clear()  # Clear the bullets list
        else:
            game_over()

    # Draw objects
    draw_enemies()
    draw_player()
    for bullet_x, bullet_y in bullets:
        pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, bullet_width, bullet_height))
    draw_score()

    # Update the display
    pygame.display.update()

    # Set FPS to 60
    clock.tick(60)




