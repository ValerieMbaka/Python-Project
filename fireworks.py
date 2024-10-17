# A python code to generate several fireworks on the screen
# Import the libraries 'turtle' for graphics and 'random' for randomness
import turtle
import random

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a turtle to draw the fireworks
firework = turtle.Turtle()
# Fastest speed
firework.speed(80)
firework.hideturtle()

# Write a function to generate a firework
def generate_firework(x, y, color):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.color(color)

    # Draw the firework explosion
    for _ in range(100):
        firework.forward(50)
        firework.backward(50)
        firework.right(50)

    # Add some randomness to the explosion
    for _ in range(1000):
        firework.forward(random.randint(60, 80))
        firework.backward(random.randint(50, 90))
        firework.right(random.randint(40, 80))

# Generate multiple fireworks
for _ in range(100):
    x = random.randint(-360, 180)
    y = random.randint(0, 180)
    color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
    generate_firework(x, y, color)

# Keep the window open
win.mainloop()