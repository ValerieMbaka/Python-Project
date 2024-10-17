import sys

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the title of the window
pygame.display.set_caption("Fireworks Simulation")

# Define some colors
BLACK = (0, 0, 0)

# Define the fireworks animation
num_fireworks = 100
firework_radius = 2
particle_radius = 1.5
explosion_radius = 50

# Create a firework class that handles individual fireworks.
# This class creates particles when the firework explodes and updates their positions.
class Firework:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = screen_height
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-5, -2)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particles = []

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1

        if self.y > screen_height:
            self.explode()

    def explode(self):
        for _ in range(100):
            particle_x = self.x + random.uniform(-explosion_radius, explosion_radius)
            particle_y = self.y + random.uniform(-explosion_radius, explosion_radius)
            particle_vx = random.uniform(-2, 2)
            particle_vy = random.uniform(-2, -2)
            self.particles.append((particle_x, particle_y, particle_vx, particle_vy))

    def draw(self):
        for particle_x, particle_y, _, _ in self.particles:
            pygame.draw.circle(screen, self.color, (int(particle_x), int(particle_y)), particle_radius)

fireworks = [Firework() for _ in range(num_fireworks)]

# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw te fireworks
    for firework in fireworks:
        firework.update()
        firework.draw()

        if firework.y > screen_height:
            fireworks.remove(firework)
            fireworks.append(Firework())

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
