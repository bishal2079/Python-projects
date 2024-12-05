from turtle import Turtle, Screen
import random
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Initialize Turtle and Screen
tim = Turtle()
screen = Screen()
screen.colormode(255)  # Enable RGB color mode

tim.speed("fastest")
def spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())  # Assign a random color to the turtle's pen
        tim.circle(60)  # Draw a circle with radius 60
        # current_head=tim.heading()
        # tim.setheading(current_head+10)
        tim.setheading(tim.heading()+10)
spirograph(5)
screen.exitonclick()

