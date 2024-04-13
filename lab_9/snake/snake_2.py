import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20
INITIAL_FPS = 10
FONT_SIZE = 24
FOOD_LIFESPAN = 10  # Food disappears after 10 seconds

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up clock for controlling game speed
clock = pygame.time.Clock()

# Define a font for displaying score and level
font = pygame.font.Font(None, FONT_SIZE)


# Function to create a random position and weight for the food
def create_random_food(snake, food=None):
    # Create a new random food position and weight
    while True:
        x = random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        food_pos = (x, y)

        # Ensure the food is not on the snake or the same as the current food position
        if food_pos not in snake and food_pos != food:
            # Assign a random weight to the food (e.g., 1 to 3 points)
            weight = random.randint(1, 3)
            # Record the start time of the food
            start_time = time.time()
            return food_pos, weight, start_time


# Function to draw the game state
def draw_game(snake, food, score, level):
    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw the food
    food_pos, weight, start_time = food
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (WINDOW_WIDTH - 120, 10))

    # Update the display
    pygame.display.update()


# Function to start the game
def start_game():
    # Initial snake and food positions
    snake = [(CELL_SIZE * 3, CELL_SIZE * 3), (CELL_SIZE * 2, CELL_SIZE * 3), (CELL_SIZE, CELL_SIZE * 3)]
    food = create_random_food(snake)

    # Initial direction is right
    direction = RIGHT

    # Initialize score and level
    score = 0
    level = 1
    speed = INITIAL_FPS

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Move the snake
        head = snake[0]
        new_head = (head[0] + direction[0] * CELL_SIZE, head[1] + direction[1] * CELL_SIZE)

        # Check for wall collisions
        if (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
                new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT):
            print("Game Over! Wall collision.")
            print(f"Final Score: {score}")
            pygame.quit()
            return

        # Check for snake collisions (self-collision)
        if new_head in snake:
            print("Game Over! Snake collision.")
            print(f"Final Score: {score}")
            pygame.quit()
            return

        # Add the new head to the snake
        snake.insert(0, new_head)

        # Check if the snake ate the food
        if new_head == food[0]:
            # Increase the score by the weight of the food
            score += food[1]

            # Increase level and speed every 4 foods
            if score % 4 == 0:
                level += 1
                speed += 2

            # Generate a new food
            food = create_random_food(snake)
        else:
            # Remove the last segment of the snake (not growing)
            snake.pop()

        # Check if the food has expired
        current_time = time.time()
        if current_time - food[2] >= FOOD_LIFESPAN:
            # If the food has been on the screen for too long, generate a new food
            food = create_random_food(snake)

        # Draw the game state
        draw_game(snake, food, score, level)

        # Control the speed of the game
        clock.tick(speed)


# Run the game
start_game()