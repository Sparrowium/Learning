import turtle

def cross_product(p0, p1, p2):
    # Calculate the cross product of vectors p0p1 and p0p2
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

def main():
    # Prompt the user for coordinates of p0, p1, and p2
    p0_x, p0_y = map(float, input("Enter coordinates for p0 (x y): ").split())
    p1_x, p1_y = map(float, input("Enter coordinates for p1 (x y): ").split())
    p2_x, p2_y = map(float, input("Enter coordinates for p2 (x y): ").split())

    # Calculate the cross product
    cp = cross_product((p0_x, p0_y), (p1_x, p1_y), (p2_x, p2_y))

    # Determine the position of p2
    if cp > 0:
        position = "left side"
    elif cp < 0:
        position = "right side"
    else:
        position = "collinear"

    # Display the result
    print(f"Point p2 is on the {position} of the line from p0 to p1.")

    # Draw the points and line
    turtle.penup()
    turtle.goto(p0_x, p0_y)
    turtle.pendown()
    turtle.dot("red")
    turtle.goto(p1_x, p1_y)
    turtle.dot("red")
    turtle.goto(p2_x, p2_y)
    turtle.dot("blue")
    turtle.exitonclick()

if __name__ == "__main__":
    main()
