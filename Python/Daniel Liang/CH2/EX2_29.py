import turtle as tt
import math


center = int(input("Enter center: "))
radius = int(input("Enter radius: "))


tt.showturtle()


tt.penup()
tt.goto(center, -radius)
tt.pendown()
tt.circle(radius)
tt.penup()
tt.goto(center, 0)
tt.pendown()
tt.write(radius ** radius * math.pi)


tt.done()