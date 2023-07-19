import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Endless Runner")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up player character
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Set up game clock
clock = pygame.time.Clock()


def game_loop():
    global player_x, player_y  # Declare player_x and player_y as global

    game_over = False
    score = 0

    # Set up obstacles
    obstacle_width = 50
    obstacle_height = 50
    obstacle_x = random.randint(0, width - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_speed = 5

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the player character
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed

        # Update obstacle position
        obstacle_y += obstacle_speed

        # Check for collision
        if obstacle_y > height:
            obstacle_x = random.randint(0, width - obstacle_width)
            obstacle_y = -obstacle_height
            score += 1

        if player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x:
                game_over = True

        # Update the display
        window.fill(black)
        pygame.draw.rect(window, white, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(window, white, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, white)
        window.blit(score_text, (10, 10))

        # Set the game speed
        clock.tick(60)  # 60 FPS

        pygame.display.update()

    # Display game over message
    game_over_text = font.render("You have collided. Game over!", True, white)
    window.blit(game_over_text, (width // 2 - 200, height // 2))
    pygame.display.update()

    pygame.time.wait(2000)  # Pause for 2 seconds before quitting
    pygame.quit()
    quit()


# Start the game loop
game_loop()
