from turtle import Turtle, Screen
import random

def color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B
def draw():
    for i in range(3, 11):
        for _ in range(i):
            R, G, B = color()
            timmy_the_turtle.color(R, G, B)
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(360 / i)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")



screen = Screen()
screen.colormode(255)
draw()
screen.exitonclick()