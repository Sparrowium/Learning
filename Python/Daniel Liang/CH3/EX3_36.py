import turtle
import random
import math

def draw_circle(radius):
    # Draw the circle
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)

def generate_random_point(radius):
    # Generate a random point within the square
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    return x, y

def is_point_inside_circle(x, y, radius):
    # Check if the point is inside the circle
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius

def main():
    radius = 100  # Diameter of the circle (side of the square)

    # Draw the circle
    turtle.speed("fastest")
    draw_circle(radius)

    # Generate a random point
    random_x, random_y = generate_random_point(radius)

    # Draw the random point
    turtle.penup()
    turtle.goto(random_x, random_y)
    turtle.pendown()
    turtle.dot("blue")

    # Check if the point is inside the circle
    if is_point_inside_circle(random_x, random_y, radius):
        message = "The point is inside the circle."
    else:
        message = "The point is outside the circle."

    # Display the result
    turtle.penup()
    turtle.goto(0, -radius - 20)
    turtle.pendown()
    turtle.write(message, align="center", font=("Arial", 12, "normal"))

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
