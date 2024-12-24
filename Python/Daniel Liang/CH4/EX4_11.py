import math, turtle



x1 = float(input("Enter x1 coordinate for triangle: "))
y1 = float(input("Enter y1 coordinate for triangle: "))
x2 = float(input("Enter x2 coordinate for triangle: "))
y2 = float(input("Enter y2 coordinate for triangle: "))
x3 = float(input("Enter x3 coordinate for triangle: "))
y3 = float(input("Enter y3 coordinate for triangle: "))

s = (math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2)
     + math.sqrt((x2 - x3) ** 2 + (y2- y3) ** 2)
     + math.sqrt((x3 - x1) ** 2 + (y3- y1) ** 2)) / 2

area = math.sqrt(s * (s - math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2))
                * (s - math.sqrt((x2 - x3) ** 2 + (y2- y3) ** 2))
                * (s - math.sqrt((x3 - x1) ** 2 + (y3- y1) ** 2)))


turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(f"p1({x1}, {y1})")
turtle.goto(x2, y2)
turtle.write(f"p2({x2}, {y2})")
turtle.goto(x3, y3)
turtle.write(f"p3({x3}, {y3})")
turtle.goto(x1, y1)

turtle.penup()
turtle.goto(x1, y1 - 50)
turtle.pendown()
turtle.write(f"the area of the triangle is {area}")
turtle.done()

