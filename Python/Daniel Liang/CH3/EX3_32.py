def is_on_line_segment(x0, y0, x1, y1, x2, y2):
    cross_product = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if abs(cross_product) < 1e-10 and (x0 <= x2 <= x1) and (y0 <= y2 <= y1):
        return True
    return False

def main():
    x0 = float(input())
    y0 = float(input())
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    if is_on_line_segment(x0, y0, x1, y1, x2, y2):
        print(f"({x2}, {y2}) is on the line segment from ({x0}, {y0}) to ({x1}, {y1})")
    else:
        print(f"({x2}, {y2}) is not on the line segment from ({x0}, {y0}) to ({x1}, {y1})")

if __name__ == "__main__":
    main()
