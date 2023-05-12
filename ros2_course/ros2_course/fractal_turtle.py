from turtle import Screen, Turtle
import random

WIDTH, HEIGHT = 800, 800

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

screen.colormode(255)

def draw_triangle(x, y, size):
    turtle.goto(x, y)
    r = random.randint(0,254)
    g = random.randint(0,254)
    b = random.randint(0,254)
    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)

    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()

def sierpinski(x, y, size):
    draw_triangle(x, y, size)

    if size > 10:
        sierpinski(x, y + size/2, size/2)
        sierpinski(x + size/2, y - size/2, size/2)
        sierpinski(x - size/2, y - size/2, size/2)



sierpinski(WIDTH/2, HEIGHT/2, HEIGHT/2)

screen.exitonclick()
