#Made By RandomCoder | Make Sure You Have Python Turtle Installed

import turtle
from turtle import *

t = turtle.Turtle()
t.speed(10)
turtle.bgcolor('grey')
t.pencolor('white')

#Circle
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()

#1st Rectangle
t.penup()
t.forward(60)

t.fillcolor('grey')
t.begin_fill()
t.left(90)
t.forward(125)
t.left(90)
t.forward(17.5)
t.left(90)
t.forward(120)
t.end_fill()

#2nd Rectangle
t.penup()
t.forward(25)
t.right(90)
t.forward(34.5)
t.right(90)

t.fillcolor('grey')
t.begin_fill()
t.forward(55)
t.left(90)
t.forward(17.5)
t.right(90)
t.forward(135)
t.right(90)
t.forward(17.5)
t.right(90)
t.forward(135)
t.end_fill()

#3rd Rectangle
t.fillcolor('white')
t.begin_fill()
t.left(90)
t.back(10)
t.forward(11.5)
t.right(90)
t.forward(32.5)
t.right(90)
t.forward(20)
t.end_fill()

t.penup()
t.forward(50)
t.right(90)
t.forward(75)
t.right(90)

t.fillcolor('grey')
t.begin_fill()
t.forward(17.5)
t.left(90)
t.forward(115)
t.left(90)
t.forward(17.5)
t.left(90)
t.forward(115)
t.end_fill()

#Text
t.penup()
t.forward(115)
t.right(90)
t.forward(27.5)
t.write('THE VILTRUM EMPIRE', font=('Arial', 12, 'bold'))
t.left(90)
t.forward(20)
t.left(90)
t.forward(40)
t.write('NEEDS YOU!', font=('Arial', 12, 'bold'))

#Border
t.right(90)
t.forward(25)
t.pendown()
t.left(90)
t.pensize(2.5)
t.forward(195)
t.left(90)
t.forward(315)
t.left(90)
t.forward(300)
t.left(90)
t.forward(315)
t.left(90)
t.forward(105)

t.hideturtle()
turtle.done()
