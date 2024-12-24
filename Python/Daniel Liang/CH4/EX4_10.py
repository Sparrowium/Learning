import turtle


turtle.showturtle()
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

#Triangle
turtle.color("red")
turtle.begin_fill()
for i in range(0, 3):
    turtle.forward(60)
    turtle.left(120)
turtle.end_fill()

#Square
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()

#Pentagon
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
for i in range(0, 5):
    turtle.forward(50)
    turtle.left(72)
turtle.end_fill()

#Hexagon
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
for i in range(0, 6):
    turtle.forward(40)
    turtle.left(60)
turtle.end_fill()

#Octagon
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for i in range(0, 8):
    turtle.forward(30)
    turtle.left(45)
turtle.end_fill()

turtle.done()
