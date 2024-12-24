import math, turtle



x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))


turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(f"({x1}, {y1})")
turtle.goto(x2, y2)
turtle.write(f"({x2}, {y2})")
turtle.done()
