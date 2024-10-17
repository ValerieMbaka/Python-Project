import sys

import pygame
import math

# from fireworks1 import screen, BLACK

# Initialise pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the title of the window
pygame.display.set_caption("Fireworks")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the fireworks animation parameters
t = 0
num_particles = 400
particles_radius = 1.5

# Function to draw a single particle
def draw_particle(i, t):
    r = 500 * math.sin(i * math.sin(t) * 2 * math.pi)
    x = math.sin(i) * r + screen_width / 2
    y = math.cos(i) * r + screen_height / 2
    # HSL color
    color = (i + 32, 100, 60)
    pygame.draw.circle(screen, color, (int(x), int(y)), particles_radius)

# Main animation loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the particles
    for i in range(num_particles):
        draw_particle(i, t)

    # Update the screen
    pygame.display.flip()

    # Increment the animation time
    t += 0.000010
    t %= 2 * math.pi

    # Cap the frame rate
    pygame.time.Clock().tick(60)