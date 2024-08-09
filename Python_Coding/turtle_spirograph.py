from turtle import Turtle, Screen
import random

def color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B

def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        R, G, B = color()
        timmy_the_turtle.color(R, G, B)
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() - size_of_gap)

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.speed("fastest")

screen = Screen()
screen.colormode(255)

spirograph(5)

screen.exitonclick()