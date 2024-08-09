from turtle import Turtle, Screen
import random

def color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B

def random_move():
    list_of_moves = ["forward", "right", "left"]
    move_choice = random.choice(list_of_moves)
    list_of_angles = [90, 180, 270, 360]
    angle_choice = random.choice(list_of_angles)

    R, G, B = color()
    timmy_the_turtle.color(R, G, B)
    timmy_the_turtle.pensize(5)
    timmy_the_turtle.speed("fastest")

    x, y = timmy_the_turtle.position()
    if x + 100 > 500 or x - 100 < -500 or y + 100 > 500 or y - 100 < -500:
        timmy_the_turtle.home()

    if move_choice == "forward":
        timmy_the_turtle.forward(30)
    elif move_choice == "right":
        timmy_the_turtle.right(angle_choice)
    elif move_choice == "left":
        timmy_the_turtle.left(angle_choice)


timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

for _ in range(200):
    random_move()

screen.exitonclick()