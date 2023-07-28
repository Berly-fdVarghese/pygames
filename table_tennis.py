import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Table Tennis Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 3, 3

# Points needed to win
WINNING_SCORE = 11

# Create paddles
paddle_a = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball direction
ball_direction = [1, 1]

# Points tracking
score_a = 0
score_b = 0

# Load font
font = pygame.font.SysFont(None, 40)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to reset the ball's position and direction
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_direction[0] = 1
    ball_direction[1] = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        paddle_b.y += PADDLE_SPEED

    # Limit paddles within the screen bounds
    paddle_a.y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle_a.y))
    paddle_b.y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle_b.y))

    # Move ball
    ball.x += ball_direction[0] * BALL_SPEED_X
    ball.y += ball_direction[1] * BALL_SPEED_Y

    # Ball collisions with walls
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_SIZE:
        ball_direction[1] *= -1

    # Ball collisions with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_direction[0] *= -1

    # Ball out of bounds
    if ball.x <= 0:
        score_b += 1
        reset_ball()

    if ball.x >= WIDTH - BALL_SIZE:
        score_a += 1
        reset_ball()

    # Check for winner
    if score_a == WINNING_SCORE or score_b == WINNING_SCORE:
        winner_text = "Player A wins!" if score_a == WINNING_SCORE else "Player B wins!"
        win_text = font.render(winner_text, True, WHITE)
        win.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Show the winner for 3 seconds
        score_a = 0
        score_b = 0
        reset_ball()

    # Clear the screen
    win.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(win, WHITE, paddle_a)
    pygame.draw.rect(win, WHITE, paddle_b)
    pygame.draw.ellipse(win, WHITE, ball)

    # Draw score
    score_text = font.render(f"Player A: {score_a}  Player B: {score_b}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
