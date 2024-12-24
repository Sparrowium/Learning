import turtle

#Face structure
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

#Nose
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.right(60)
turtle.forward(60)
turtle.right(120)
turtle.forward(60)
turtle.right(120)
turtle.forward(60)
turtle.right(60)

#eyes
turtle.penup()
turtle.goto(-50, 30)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 30)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

#Mouth
turtle.penup()
turtle.goto(-40, -40)
turtle.pendown()
turtle.right(40)
turtle.forward(50)
turtle.left(80)
turtle.forward(50)

turtle.done()

