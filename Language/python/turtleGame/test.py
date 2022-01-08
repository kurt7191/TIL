import turtle as t
import random


def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_right():
    t.setheading(0)
    t.forward(10)


def make_triangle(n):
    t.setheading(360/n)
    t.forward(100)


t.speed(0)
t.shape('turtle')
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_right,"Right")

t.listen()

make_triangle(3)
