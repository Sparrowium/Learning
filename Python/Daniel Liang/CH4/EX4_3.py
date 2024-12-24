import math

def great_circle_distance(lon1, lat1, lon2, lat2):
    # Convert degrees to radians
    lon1_rad, lat1_rad, lon2_rad, lat2_rad = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = 6371 * c

    return distance_km

# Coordinates for the cities
atlanta = (-84.387982, 33.748995)
orlando = (-81.379234, 28.538336)
savannah = (-81.091203, 32.080898)
charlotte = (-80.843127, 35.227087)

# Calculate distances
distance_atl_orl = great_circle_distance(*atlanta, *orlando)
distance_sav_cha = great_circle_distance(*savannah, *charlotte)
distance_cha_atl = great_circle_distance(*charlotte, *atlanta)

# Compute the area of the polygon formed by these cities
s = (distance_atl_orl + distance_sav_cha + distance_cha_atl) / 2
area_km2 = math.sqrt(s * (s - distance_atl_orl) * (s - distance_sav_cha) * (s - distance_cha_atl))

print(f"The estimated area enclosed by these four cities is approximately {area_km2:.2f} square kilometers.")
