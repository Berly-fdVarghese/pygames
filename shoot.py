import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PLAYER_COLOR = BLUE
ENEMY_COLOR = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Enemies
enemy_size = 50
num_enemies = 5  # Number of enemies to create
enemies = []  # List to store enemy objects

# Enemy speed
enemy_speed = 3  # Initial enemy speed
enemy_speed_increment = 0.5  # Speed increment for each difficulty level

for _ in range(num_enemies):
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = random.randint(-HEIGHT, 0)
    enemies.append([enemy_x, enemy_y, enemy_size, enemy_size, enemy_speed])

# Score
score = 0
score_font = pygame.font.Font(None, 36)

# Game Over
game_over = False
game_over_font = pygame.font.Font(None, 48)

# Difficulty
difficulty_level = 1
difficulty_increase_interval = 2000  # milliseconds
last_difficulty_increase_time = pygame.time.get_ticks()


# Game Loop
running = True
clock = pygame.time.Clock()

def increase_difficulty():
    global enemy_speed, player_speed, difficulty_level
    enemy_speed += enemy_speed_increment
    player_speed +=0.2
    difficulty_level += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    window.fill(WHITE)

    pygame.draw.rect(window, PLAYER_COLOR, (player_x, player_y, player_size, player_size))

    for enemy in enemies:
        pygame.draw.rect(window, ENEMY_COLOR, enemy[:4])
        enemy[1] += enemy[4]
        if enemy[1] > HEIGHT:
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = random.randint(-HEIGHT, 0)
            score += 1

        if player_y < enemy[1] + enemy_size and player_y + player_size > enemy[1]:
            if player_x < enemy[0] + enemy_size and player_x + player_size > enemy[0]:
                score -= 2
                game_over = True

    # Render and display the score
    score_text = score_font.render("Score: " + str(score), True, BLUE)
    window.blit(score_text, (10, 10))

    if score >= 100:
        score_100_sound.play()
        score = 0  # Reset the score to prevent repeated sound playing

    if game_over:
        game_over_text = game_over_font.render("You have collided. You lost the game.", True, BLUE)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(game_over_text, game_over_text_rect)

        # Display the message for a few seconds
        pygame.display.update()
        pygame.time.wait(3000)

        running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_difficulty_increase_time >= difficulty_increase_interval:
        increase_difficulty()
        last_difficulty_increase_time = current_time

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
