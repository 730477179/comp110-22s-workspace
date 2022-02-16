
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50) #changing speed
leo.hideturtle() #hiding the turtle
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.penup() # always goes before the goto line
leo.goto(45,60) # moves pen to a new coordinate
colormode(255) # enables RGB mode
leo.color(99, 204, 250) # adds the color to allow for creativity
leo.pendown() # moves pen to a new point


leo.begin_fill() #allows us to begin fill
i: int = 0
while (i < 3):
    leo.forward(300) # tells how many units forward
    leo.left(120) #tells angle of tilt
    i = i + 1
leo.end_fill() #allows us to end fill




bob: Turtle = Turtle()

side_length: float = 300.00

bob.penup()
bob.goto(45,60)
bob.pendown()

i: int = 0
colormode(255)
bob.color("red")
while (i < 20): 
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97
bob.pendown() 
done()