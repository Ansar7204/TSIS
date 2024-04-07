import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ERASER_WIDTH = 20  # Width of the eraser line

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint Program")

# Variables
drawing = False
last_pos = None
color = WHITE
draw_shape = 'line'
erasing = False  # Flag to indicate if the eraser is active

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
            elif event.key == pygame.K_l:
                draw_shape = 'line'
            elif event.key == pygame.K_c:
                draw_shape = 'circle'
            elif event.key == pygame.K_r:
                draw_shape = 'rectangle'
            elif event.key == pygame.K_s:
                draw_shape = 'square'
            elif event.key == pygame.K_h:
                draw_shape = 'rhombus'
            elif event.key == pygame.K_t:
                draw_shape = 'equilateral_triangle'
            elif event.key == pygame.K_e:
                erasing = True
                color = BLACK
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            erasing = False
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            erasing = False  
        elif event.type == pygame.MOUSEMOTION and (drawing or erasing):
            if draw_shape == 'line' and not erasing:
                pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, color, last_pos, pos, 3)
                last_pos = pos
            elif draw_shape == 'circle' and not erasing:
                pos = pygame.mouse.get_pos()
                dx = pos[0] - last_pos[0]
                dy = pos[1] - last_pos[1]
                radius = int((dx ** 2 + dy ** 2) ** 0.5)
                pygame.draw.circle(screen, color, last_pos, radius, 3)
            elif draw_shape == 'rectangle' and not erasing:
                pos = pygame.mouse.get_pos()
                width = pos[0] - last_pos[0]
                height = pos[1] - last_pos[1]
                pygame.draw.rect(screen, color, pygame.Rect(last_pos[0], last_pos[1], width, height), 3)
            elif draw_shape == 'square' and not erasing:
                pos = pygame.mouse.get_pos()
                side_length = abs(pos[0] - last_pos[0])
                pygame.draw.rect(screen, color, pygame.Rect(last_pos[0], last_pos[1], side_length, side_length), 3)
            elif draw_shape == 'rhombus' and not erasing:
                pos = pygame.mouse.get_pos()
                # Calculate the midpoints of the opposite sides
                midpoint_x = (last_pos[0] + pos[0]) / 2
                midpoint_y = (last_pos[1] + pos[1]) / 2
                # Calculate the offsets for the rhombus points
                offset_x = abs(pos[0] - last_pos[0]) / 2
                offset_y = abs(pos[1] - last_pos[1]) / 2
                # Define the rhombus points
                points = [
                    (midpoint_x, last_pos[1] + offset_y),
                    (last_pos[0] + offset_x, midpoint_y),
                    (midpoint_x, pos[1] - offset_y),
                    (pos[0] - offset_x, midpoint_y)
                ]
                pygame.draw.polygon(screen, color, points, 3)
            elif draw_shape == 'equilateral_triangle' and not erasing:
                pos = pygame.mouse.get_pos()
                dx = pos[0] - last_pos[0]
                dy = pos[1] - last_pos[1]
                side_length = int((dx ** 2 + dy ** 2) ** 0.5)
                height = int(math.sqrt(3) / 2 * side_length)
                midpoint = ((last_pos[0] + pos[0]) / 2, (last_pos[1] + pos[1]) / 2)
                points = [
                    (midpoint[0], midpoint[1] - height),
                    (midpoint[0] + side_length / 2, midpoint[1] + height / 2),
                    (midpoint[0] - side_length / 2, midpoint[1] + height / 2)
                ]
                pygame.draw.polygon(screen, color, points, 3)
            elif erasing:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, color, pos, ERASER_WIDTH)

    pygame.display.flip()

pygame.quit()
sys.exit()