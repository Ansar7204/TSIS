import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Ball Movement')

# Define the ball properties
ball_pos = [screen_width // 2, screen_height // 2]  # Initial position of the ball
ball_radius = 25
ball_color = (255, 0, 0)  # Red color

# Main game loop
running = True
while running:
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the ball based on arrow key presses
            if event.key == pygame.K_UP:
                if ball_pos[1] - ball_radius > 0:  # Check if the ball is within the screen boundaries
                    ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                if ball_pos[1] + ball_radius < screen_height:  # Check if the ball is within the screen boundaries
                    ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                if ball_pos[0] - ball_radius > 0:  # Check if the ball is within the screen boundaries
                    ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_pos[0] + ball_radius < screen_width:  # Check if the ball is within the screen boundaries
                    ball_pos[0] += 20

    # Check if the user wants to quit
    if not running:
        pygame.quit()
        sys.exit()