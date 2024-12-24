import turtle as tt


radius = int(input("Enter radius: "))


tt.showturtle()
tt.circle(radius)
tt.right(180)
tt.circle(radius)
tt.penup()
tt.forward(radius * 2)
tt.pendown()
tt.circle(radius)
tt.right(180)
tt.circle(radius)


tt.done()