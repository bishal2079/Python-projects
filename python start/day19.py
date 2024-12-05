from turtle import Turtle,Screen
import random
# tur=Turtle()
# tim=Turtle()
# for _ in range(4):
#     tur.forward(100)
#     tur.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

direction = [0, 90, 180, 270]

# Set up turtle
turk = Turtle()
turk.pensize(15)
turk.speed("fastest")

# Set up the screen for RGB mode
screen = Screen()
screen.colormode(255)

for _ in range(200):
    turk.color(random_color())  # Generate and set a random color
    turk.forward(30)
    turk.setheading(random.choice(direction))

screen.exitonclick()

# Function to draw shapes
# def draw_shape(turtle_obj, num_sides):
#     """
#     Draws a regular polygon with a specified number of sides.

#     Parameters:
#     - turtle_obj: The turtle object used for drawing.
#     - num_sides: The number of sides of the polygon.
#     """
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle_obj.forward(100)
#         turtle_obj.right(angle)

# # Custom Turtle class with interactive methods
# class MyTurtle(Turtle):
#     def glow(self, x, y):
#         self.fillcolor("red")

#     def unglow(self, x, y):
#         self.fillcolor("")

# # Main program
# screen = Screen()  # Create a Screen object
# kur = MyTurtle()   # Create a custom turtle instance
# kur.speed(5)

# # Draw shapes with random colors
# for shape_side in range(3, 11):
#     kur.color(random.choice(colors))
#     draw_shape(kur, shape_side)

# # Bind events for interaction
# kur.onclick(kur.glow)          # Clicking changes fillcolor to red
# screen.onclick(lambda x, y: kur.unglow(x, y))  # Clicking elsewhere resets fillcolor

# # Keep the window open
# screen.mainloop()
