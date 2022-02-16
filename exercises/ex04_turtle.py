"""A piece of Suburbia"""
__author__ = "730477179."

from random import randint
from turtle import Turtle, begin_fill, colormode, done, fillcolor, forward

def main() -> None:
    """The beginning of my picture"""
    house: Turtle = Turtle()
    draw_base_of_house_or_windows(house, -10, 10, 100)
    draw_base_of_house_or_windows(house, 120, 10, 100)
    """A new house in construction in this neighborhood. I am trying for a house with a different size to be introduced"""
    draw_base_of_house_or_windows(house, 400, 10, randint )

    draw_roofs(house,-10,10,75)
    draw_roofs(house,120,10,75)

    draw_sun(house, 300, 300, 40)

    draw_doors(house, 60, -20, 50 )
    draw_doors(house, 190 ,-20, 50 )

    draw_base_of_house_or_windows(house, -5, 5, 20)
    draw_base_of_house_or_windows(house, 65, 5, 20)
    draw_base_of_house_or_windows(house, 195, 5, 20)
    draw_base_of_house_or_windows(house, 125, 5, 20)
    done()


def draw_base_of_house_or_windows(house: Turtle, x: float, y: float, width: float) -> None:
    """Draw the bases for the houses and windows"""
    house.penup()
    house.goto(x, y) 
    house.setheading(0.0)
    house.pendown()
    i: int = 0
    while i < 4:
        house.begin_fill
        colormode(255)
        house.fillcolor(246, 150, 232)
        house.color("pink")
        house.forward(width)
        house.right(90)
        i = i + 1

def draw_roofs(house: Turtle, x: float, y: float, width: float) -> None:
    """Draws triangles for roofs"""
    colormode(255)
    house.color("red")
    house.penup()
    house.goto(x, y) 
    house.setheading(0.0)
    house.pendown()
    house.left(45)
    house.forward(width)
    house.right(45)


def draw_sun(house: Turtle, x: float, y: float, width: float) -> None:
    """Draws the sun """
    house.penup()
    house.goto(x, y) 
    house.setheading(0.0)
    house.pendown()
    i:int = 0
    while i < 9:
        colormode(255)
        house.color("orange")
        house.right(45)
        house.forward(45)
        i = i + 1
    house.begin_fill()
    colormode(255)
    house.fillcolor(244, 232, 25)
    house.end_fill 
        
def draw_doors(house: Turtle, x: float, y: float, width: float) -> None:
    """Draws Rectangles for Doors"""
    house.penup()
    house.goto(x, y) 
    house.setheading(0.0)
    house.pendown()
    i:int = 0
    while i < 2:
        colormode(255)
        house.color("blue")
        house.begin_fill()
        house.fillcolor(150,188,246)
        house.right(90)
        house.forward(70)
        house.right(90)
        house.forward(40)
        i = i + 1
        house.end_fill 
    

if __name__ == "__main__": 
        main()




#work on clsing roofs 
# work on filling in color
# randint isn't working?