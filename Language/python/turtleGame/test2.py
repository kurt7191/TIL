import turtle as t
import random

t.shape('turtle')
t.speed(0)

distance = random.randint(50,200)


def gogo(distance):
    for x in range(3):
        t.forward(distance)
        t.left(360/3)
        
gogo(distance)
