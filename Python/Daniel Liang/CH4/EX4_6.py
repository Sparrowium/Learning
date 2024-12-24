import turtle


length = float(input("Enter the length of the star: "))

# Set up the turtle screen
turtle.speed("fastest")
turtle.hideturtle()

# Draw the star
for _ in range(5):
    turtle.forward(length)
    turtle.right(144)

turtle.done()
