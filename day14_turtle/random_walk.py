import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def rgb_color():
        r=random.randint(0,10)
        g=random.randint(0,150)
        b=random.randint(0,255)
        random_color=(r,g,b)
        return random_color
    
for _ in range(200):
    tim.color(rgb_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

