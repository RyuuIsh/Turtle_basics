from turtle import Turtle, Screen
import random

# Initialize turtle and screen
jim = Turtle()
screen = Screen()
screen.colormode(255)  # Set colormode for RGB colors
jim.shape("turtle")
jim.speed("fastest")

# Draw a square
jim.color("DarkOrchid1")
for _ in range(4):
    jim.forward(100)
    jim.right(90)

# Draw a dashed line
for _ in range(15):
    jim.forward(10)
    jim.penup()
    jim.forward(10)
    jim.pendown()

# Draw multiple polygons
polygons = [
    (3, "blue"),
    (4, "yellow"),
    (5, "red"),
    (6, "grey"),
    (7, "green"),
    (8, "orange"),
    (9, "black"),
    (10, "CornflowerBlue")
]
for sides, color in polygons:
    jim.color(color)
    for _ in range(sides):
        jim.forward(50)
        jim.right(360 / sides)

# Draw a random walk
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
jim.pensize(5)

for _ in range(200):
    jim.color(random.choice(colours))
    jim.forward(10)
    jim.setheading(random.choice(directions))

# Generate random RGB colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

jim.pensize(1)
# Draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)

draw_spirograph(5)

# Exit on click
screen.exitonclick()
