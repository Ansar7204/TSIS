import pygame
import sys
from datetime import datetime

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
clock_image = pygame.image.load('clock.png')
second_hand_image = pygame.image.load('left.png')
minute_hand_image = pygame.image.load('right.png')

# Set the center of the clock
clock_rect = clock_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    # Calculate the angles for the hands
    second_angle = -((seconds * 6)+ 4)
    minute_angle = -(((minutes+9) * 6) )

    # Rotate the images
    rotated_second_hand = pygame.transform.rotate(second_hand_image, second_angle)
    rotated_minute_hand = pygame.transform.rotate(minute_hand_image, minute_angle)

    # Get the rectangles for the rotated images
    rotated_hour_rect = rotated_second_hand.get_rect(center=clock_rect.center)
    rotated_minute_rect = rotated_minute_hand.get_rect(center=clock_rect.center)

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the clock and hands
    screen.blit(clock_image, clock_rect)
    screen.blit(rotated_second_hand, rotated_hour_rect)
    screen.blit(rotated_minute_hand, rotated_minute_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
sys.exit()