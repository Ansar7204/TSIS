import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the display
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_block = 10
initial_snake_speed = 15

# Set up the font
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

class Food:
    def __init__(self):
        self.x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        self.weight = random.randint(1, 5)
        self.spawn_time = time.time()

    def draw(self):
        pygame.draw.rect(dis, green, [self.x, self.y, snake_block, snake_block])

    def is_expired(self):
        return time.time() - self.spawn_time > 5

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food = Food()

    level = 1
    foods_eaten = 0
    snake_speed = initial_snake_speed

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Check for collision with food
        if x1 == food.x and y1 == food.y:
            Length_of_snake += food.weight
            foods_eaten += 1
            food = Food()  # Spawn a new food item

            if foods_eaten % 4 == 0:
                level += 1
                snake_speed = initial_snake_speed + level
                foods_eaten = 0

        # Draw food if it's not expired
        if not food.is_expired():
            food.draw()
        else:
            food = Food()  # Spawn a new food item if the current one is expired

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        display_level(level)
        display_speed(snake_speed)

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def display_level(lvl):
    value = font_style.render("Level: " + str(lvl), True, yellow)
    dis.blit(value, [0, 20])

def display_speed(speed):
    value = font_style.render("Speed: " + str(speed), True, yellow)
    dis.blit(value, [0, 40])

gameLoop()