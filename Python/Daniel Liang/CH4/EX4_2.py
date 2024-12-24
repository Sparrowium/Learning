import math

# Constants
EARTH_RADIUS_KM = 6371.01

def main():
    # Input latitude and longitude for point 1
    lat1_deg = float(input("Enter the latitude of point 1 (degrees): "))
    lon1_deg = float(input("Enter the longitude of point 1 (degrees): "))

    # Input latitude and longitude for point 2
    lat2_deg = float(input("Enter the latitude of point 2 (degrees): "))
    lon2_deg = float(input("Enter the longitude of point 2 (degrees): "))

    # Convert degrees to radians
    lat1_rad = math.radians(lat1_deg)
    lon1_rad = math.radians(lon1_deg)
    lat2_rad = math.radians(lat2_deg)
    lon2_rad = math.radians(lon2_deg)

    # Compute the great circle distance
    central_angle = math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) +
                              math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lon1_rad - lon2_rad))
    distance_km = EARTH_RADIUS_KM * central_angle

    print(f"The great circle distance between the two points is approximately {distance_km:.2f} km.")

if __name__ == "__main__":
    main()
