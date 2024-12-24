class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def check_overlap(rect1, rect2):
    # Calculate the coordinates of the corners for both rectangles
    rect1_top_left = (rect1.x - rect1.width / 2, rect1.y + rect1.height / 2)
    rect1_bottom_right = (rect1.x + rect1.width / 2, rect1.y - rect1.height / 2)
    rect2_top_left = (rect2.x - rect2.width / 2, rect2.y + rect2.height / 2)
    rect2_bottom_right = (rect2.x + rect2.width / 2, rect2.y - rect2.height / 2)

    # Check if rect2 is inside rect1 or overlaps with it
    if (rect2_top_left[0] >= rect1_top_left[0] and
            rect2_top_left[1] <= rect1_top_left[1] and
            rect2_bottom_right[0] <= rect1_bottom_right[0] and
            rect2_bottom_right[1] >= rect1_bottom_right[1]):
        return "inside"
    else:
        return "overlaps"

def main():
    # Prompt the user for rectangle information
    x1, y1, width1, height1 = map(float, input("Enter center x, y, width, and height for rectangle 1: ").split())
    x2, y2, width2, height2 = map(float, input("Enter center x, y, width, and height for rectangle 2: ").split())

    # Create Rectangle objects
    rect1 = Rectangle(x1, y1, width1, height1)
    rect2 = Rectangle(x2, y2, width2, height2)

    # Check overlap
    result = check_overlap(rect1, rect2)
    print(f"The second rectangle {result} with the first rectangle.")

if __name__ == "__main__":
    main()

