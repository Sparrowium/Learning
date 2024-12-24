import turtle

turtle.showturtle()

turtle.color("Blue")
turtle.forward(60)
turtle.penup()
turtle.forward(40)
turtle.write("3")

turtle.setpos(0, 0)
turtle.pendown()
turtle.color("Red")
turtle.left(90)
turtle.forward(80)
turtle.penup()
turtle.forward(20)
turtle.write("12")

turtle.setpos(0, 0)
turtle.pendown()
turtle.color("Green")
turtle.left(90)
turtle.forward(40)
turtle.penup()
turtle.forward(60)
turtle.pendown()
turtle.write("9")
turtle.color("Black")
turtle.penup()

turtle.setpos(-100, 0)
turtle.pendown()
turtle.left(90)
turtle.circle(100)

turtle.done()