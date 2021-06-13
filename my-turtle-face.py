##---DON TU TURTLE EXERCISE-- My Turtle Face--##

import turtle
import random

screen=turtle.Screen()
# screen.setup(width=800, height=800, startx=0, starty=0)
screen.bgcolor("#4682b2")
screen.title("LaGCC")

#My Turtle Environment
my_turtle=turtle.Turtle()
my_turtle.pensize(3)
my_turtle.speed(8)

# Big Circle - center
my_turtle.penup()
my_turtle.setx(0)
my_turtle.sety(-150)
# my_turtle.goto(-200, -200)
my_turtle.color("black", "yellow")
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.circle(170)
my_turtle.end_fill()


# Circle - center
my_turtle.penup()
my_turtle.goto(85, 75)
my_turtle.color("#4682b4", "red")
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.circle(15)
my_turtle.end_fill()


# Circle - center
my_turtle.penup()
my_turtle.goto(-85, 75)
my_turtle.color("#4682b4", "red")
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.circle(15)
my_turtle.end_fill()

#triangle - Nose
my_turtle.penup()
my_turtle.pencolor("red")
my_turtle.goto(33,20)
my_turtle.begin_fill()
for items in range(3):
    my_turtle.right(120)
    my_turtle.forward(50)
    my_turtle.penup()      
my_turtle.end_fill()

#Mouth
my_turtle.goto(-35, -80)
my_turtle.pensize(8)
my_turtle.pencolor("red")
my_turtle.pendown()
my_turtle.forward(80)
my_turtle.hideturtle()


turtle.done()
my_turtle.mainloop()
