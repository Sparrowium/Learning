import turtle

def draw_rectangle(width, height):
    # Draw the rectangle centered at (0, 0)
    turtle.penup()
    turtle.goto(-width / 2, -height / 2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def main():
    # Prompt the user for the point coordinates
    x, y = map(float, input("Enter the coordinates of the point (x y): ").split())

    # Set up the turtle screen
    turtle.speed("fastest")
    turtle.hideturtle()

    # Draw the rectangle
    draw_rectangle(100, 50)

    # Draw the point
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot("blue")

    # Check if the point is inside the rectangle
    if abs(x) <= 50 and abs(y) <= 25:
        message = "The point is inside the rectangle."
    else:
        message = "The point is outside the rectangle."

    # Display the result
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.write(message, align="center", font=("Arial", 12, "normal"))

    turtle.done()

if __name__ == "__main__":
    main()
