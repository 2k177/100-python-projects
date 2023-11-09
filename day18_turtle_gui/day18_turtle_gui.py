import turtle as t
import random


tony = t.Turtle()
tony.shape("turtle")
tony.color("red")

#draw a square
# tony.forward(100)
# tony.left(90)
# tony.forward(100)
# tony.left(90)
# tony.forward(100)
# tony.left(90)
# tony.forward(100)
# tony.left(90)
#
# #use dotted line
# for _ in range(15):
#     tony.forward(10)
#     tony.penup()
#     tony.forward(10)
#     tony.pendown()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# #draw any shape
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tony.forward(100)
#         tony.right(angle)
#
# for shape_side_n in range(3, 10):
#     tony.color(random.choice(colours))
#     draw_shape(shape_side_n)

#walk in a random direction
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
t.colormode(255)
# directions = [0, 90, 180, 270]
# #set pen size
# tony.pensize(15)
tony.speed("fastest")
#
# for _ in range(200):
#     tony.color(random_color())
#     tony.forward(30)
#     tony.setheading(random.choice(directions))

#Challenge 5 - Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tony.color(random_color())
        tony.circle(100)
        tony.setheading(tony.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()