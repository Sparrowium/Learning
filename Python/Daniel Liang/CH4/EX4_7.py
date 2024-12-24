import turtle



# Set up the turtle screen
turtle.speed("fastest")
turtle.hideturtle()

turtle.fillcolor('red')
turtle.begin_fill()
# Draw the octagon
for _ in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()
# Write "STOP" inside the octagon
turtle.penup()
turtle.goto(50, -140)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", align="center", font=("Arial", 24, "bold"))

turtle.done()


