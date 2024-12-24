import math

def calculate_angle(x1, y1, x2, y2):
    # Calculate the dot product of vectors (x1, y1) and (x2, y2)
    dot_product = x1 * x2 + y1 * y2
    
    # Calculate the magnitudes of vectors (x1, y1) and (x2, y2)
    magnitude1 = math.sqrt(x1**2 + y1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2)
    
    # Calculate the cosine of the angle between the vectors
    cosine_theta = dot_product / (magnitude1 * magnitude2)
    
    # Calculate the angle in radians
    angle_radians = math.acos(cosine_theta)
    
    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees

def main():
    # Input the coordinates of the four points
    x1, y1 = map(float, input("Enter coordinates for p1 (x1 y1): ").split())
    x2, y2 = map(float, input("Enter coordinates for p2 (x2 y2): ").split())
    x3, y3 = map(float, input("Enter coordinates for p3 (x3 y3): ").split())
    x4, y4 = map(float, input("Enter coordinates for p4 (x4 y4): ").split())
    
    # Calculate the vectors AB, BC, and CD
    AB_x = x2 - x1
    AB_y = y2 - y1
    BC_x = x3 - x2
    BC_y = y3 - y2
    CD_x = x4 - x3
    CD_y = y4 - y3
    
    # Calculate the angles
    angle_A = calculate_angle(AB_x, AB_y, -BC_x, -BC_y)
    angle_B = calculate_angle(BC_x, BC_y, -CD_x, -CD_y)
    angle_C = calculate_angle(CD_x, CD_y, -AB_x, -AB_y)
    angle_D = 360 - angle_A - angle_B - angle_C
    
    # Display the angles
    print(f"Angle A: {angle_A:.2f}°")
    print(f"Angle B: {angle_B:.2f}°")
    print(f"Angle C: {angle_C:.2f}°")
    print(f"Angle D: {angle_D:.2f}°")

if __name__ == "__main__":
    main()
