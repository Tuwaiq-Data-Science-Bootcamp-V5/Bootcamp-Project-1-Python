# Snake Game in Pygame

This document explains the code for a simple Snake game implemented using the Pygame library in Python.

## Ingame screenshots:
<img  width="400" height="400"  alt="Screen Shot 1444-06-17 at 9 20 35 AM"  src=p1.png>

<img  width="400" height="400"  alt="Screen Shot 1444-06-17 at 9 20 35 AM"  src=p2.png>

<img  width="400" height="400"  alt="Screen Shot 1444-06-17 at 9 20 35 AM"  src=p3.png>


## Initialization

```python
import pygame
import random

pygame.init()
```

- We begin by importing the necessary libraries, Pygame for game development and the random module for generating random numbers.

## Colors and Display Configuration

```python
# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
```

- These lines define a set of RGB color values that will be used throughout the game.

```python
# Screen width & height
disp_width = 600
disp_height = 400
```

- These lines specify the dimensions of the game display.

```python
# Creating the display
dis = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Snake Game')
```

- We create the game display window using Pygame and set its title.

```python
# Clock reference for synchronization
clock = pygame.time.Clock()
```

- We initialize a clock object to control the frame rate of the game.

## Snake Attributes and Fonts

```python
# Snake's attributes
snake_block = 10
snake_speed = 10
```

- These lines define attributes of the snake, including the size of a snake segment and its movement speed.

```python
# Font styles
font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 20)
```

- We set up font styles for displaying text in the game.

## Lambda Function for Displaying Score

```python
display_score = lambda score: dis.blit(score_font.render("Your Score: " + str(score), True, yellow), [0, 0])
```

- This is a lambda function that takes a score as input and displays it on the game screen.

## Snake and Message Functions

```python
def our_snake(snake_block, snake_list):
    # Function to draw the snake on the screen
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    # Function to display messages on the screen
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disp_width / 6, disp_height / 3])
```

- These functions handle drawing the snake on the screen and displaying messages, such as game over messages.

## Main Game Loop

```python
def gameLoop():
    game_over = False
    game_close = False
```

- The `gameLoop` function is where the main game logic resides. It initializes game state variables.

```python
    while not game_over:
```

- The game runs in a loop until the `game_over` flag is set to `True`.

## Handling Game Over and Restart

```python
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            display_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
```

- When the game ends, this section of code displays a game over message and allows the player to restart or quit the game.

## Handling User Input

```python
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
```

- This part of the code handles user input to control the snake's movement based on arrow key presses.

## Checking Boundaries and Collision

```python
        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True
```

- It checks if the snake hits the boundaries of the game screen and triggers a game over if it does.

```python
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
```

- This code checks if the snake collides with itself, causing a game over.

## Displaying Score and Updating the Game

```python
        our_snake(snake_block, snake_List)
        display_score(Length_of_snake - 1)
        pygame.display.update()
```

- This section updates the display with the snake's position and the player's score.

## Food Consumption and Growing the Snake

```python
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
```

- It handles the snake consuming food, regenerating the food, and increasing the snake's length.

## Controlling Frame Rate

```python
        clock.tick(snake_speed)
```

- This controls the frame