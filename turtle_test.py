from turtle import Turtle, Screen
from random import choice
from colours_random import color_list

pointer = Turtle()
pointer.shape("circle")
pointer.penup()
pointer.hideturtle()
pointer.speed(35)
pointer.setposition(-460, -383)
starting_x = -460
starting_y = -383
while True:
    pointer.pensize(15)
    pointer.dot(17, choice(color_list))
    pointer.forward(24)
    if pointer.xcor() == 476.00:
        starting_y += 24
        pointer.setx(starting_x)
        pointer.sety(starting_y)
    if pointer.ycor() == 409.0:
        break

screen = Screen()
screen.exitonclick()