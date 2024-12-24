import turtle
import math

def draw_circle(x, y, radius):
    # Draw a circle centered at (x, y) with the given radius
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def check_overlap(circle1, circle2):
    # Calculate the distance between the centers
    distance = math.sqrt((circle2[0] - circle1[0])**2 + (circle2[1] - circle1[1])**2)

    # Check if the second circle is inside or overlaps with the first
    if distance + circle2[2] <= circle1[2]:
        return "inside"
    else:
        return "overlaps"

def main():
    # Prompt the user for circle information
    x1, y1, r1 = map(float, input("Enter center x, y, and radius for circle 1: ").split())
    x2, y2, r2 = map(float, input("Enter center x, y, and radius for circle 2: ").split())

    # Set up the turtle screen
    turtle.speed("fastest")
    turtle.hideturtle()

    # Draw the circles
    draw_circle(x1, y1, r1)
    draw_circle(x2, y2, r2)

    # Check overlap
    result = check_overlap((x1, y1, r1), (x2, y2, r2))
    print(f"The second circle {result} with the first circle.")

    turtle.done()

if __name__ == "__main__":
    main()
