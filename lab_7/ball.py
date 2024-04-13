import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Ball parameters
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2

# Movement speed
speed = 20

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - speed >= ball_radius:
                    ball_y -= speed
            elif event.key == pygame.K_DOWN:
                if ball_y + speed <= screen_height - ball_radius:
                    ball_y += speed
            elif event.key == pygame.K_LEFT:
                if ball_x - speed >= ball_radius:
                    ball_x -= speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + speed <= screen_width - ball_radius:
                    ball_x += speed

    # Fill the screen with white color
    screen.fill(white)

    # Draw the ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()