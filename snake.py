import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the width and height of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
game_window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')

# Set the speed of the snake
snake_speed = 15

# Define the size of each snake segment
snake_block_size = 20

# Initialize clock object to control the frame rate
clock = pygame.time.Clock()

# Define the font style
font_style = pygame.font.SysFont(None, 50)


def score(score_val):
    """Display the score on the screen."""
    value = font_style.render("Your Score: " + str(score_val), True, WHITE)
    game_window.blit(value, [window_width / 6, window_height / 6])


def snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(game_window, BLACK, [x[0], x[1], snake_block, snake_block])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initialize the position and movement of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the snake's body segments
    snake_list = []
    snake_length = 1

    # Generate the initial position of the food
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            game_window.fill(BLUE)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            game_window.blit(message, [window_width / 6, window_height / 3])
            score(snake_length - 1)
            pygame.display.update()

            # Wait for user input to either quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Update the position of the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block_size:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block_size:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block_size:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block_size:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check for collisions with boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change
        game_window.fill(BLUE)
        pygame.draw.rect(game_window, GREEN, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Truncate the snake list if it exceeds the length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with the snake's body
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Update the snake and food on the screen
        snake(snake_block_size, snake_list)
        score(snake_length - 1)
        pygame.display.update()

        # Check for collisions with the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            snake_length += 1

        # Set the frame rate of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game loop
game_loop()
