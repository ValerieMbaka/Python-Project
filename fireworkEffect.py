import sys
import pygame
import math

# Initialize pygame
pygame.init()

# Set up the screen dimensions
scrn_width, scrn_height = 800, 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))

# Set up the title of the window
pygame.display.set_caption('Firework Effect')

# Define some colors
black = (0, 0, 0)

# Define the firework animation parameters
num_circles = 400
circle_radius = 1.5
amplitude = 500
frequency = 2 * math.pi

class Circle:
    def __init__(self, i):
        self.i = i
        self.x = math.sin(i) * amplitude + scrn_width / 2
        self.y = math.cos(i) * amplitude + scrn_height / 2
        self.color = (i + 32, 100, 60)
        self.radius = circle_radius

    def update(self, t):
        self.x = math.sin(self.i + t) * amplitude + scrn_width / 2
        self.y = math.cos(self.i + t) * amplitude + scrn_height / 2
        self.radius += circle_radius

    def draw(self):
        pygame.draw.circle(scrn, self.color, (int(self.x), int(self.y)), self.radius)

circles = [Circle(i) for i in range(num_circles)]

# Main animation loop
t = 0
while True:
    # Handles events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    scrn.fill(black)

    # Update and draw the circles
    for circle in circles:
        circle.update(t)
        circle.draw()

    # Update the screen
    pygame.display.flip()

    # Increment the animation time
    t += 0.000010
    t %= 2 * math.pi

    # Cap the frame rate
    pygame.time.Clock().tick(60)