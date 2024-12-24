
x1 = float(input("Enter the x-coordinate of the center: "))
y1 = float(input("Enter the y-coordinate of the center: "))
w1 = float(input("Enter the width of the rectangle: "))
h1 = float(input("Enter the height of the rectangle: "))
x2 = float(input("Enter the x2-coordinate of the center: "))
y2 = float(input("Enter the y2-coordinate of the center: "))
w2 = float(input("Enter the width2 of the rectangle: "))
h2 = float(input("Enter the height2 of the rectangle: "))
# Calculate edges
left1, right1 = x1 - w1 / 2, x1 + w1 / 2
top1, bottom1 = y1 + h1 / 2, y1 - h1 / 2
left2, right2 = x2 - w2 / 2, x2 + w2 / 2
top2, bottom2 = y2 + h2 / 2, y2 - h2 / 2
# Check for overlap
if (right1 < left2 or left1 > right2) or (top1 < bottom2 or bottom1 > top2):
    print("No overlap")
elif left2 >= left1 and right2 <= right1 and top2 <= top1 and bottom2 >= bottom1:
    print("Rectangle 2 is fully contained in Rectangle 1")
else:
    print("Overlap")