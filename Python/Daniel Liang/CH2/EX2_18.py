import datetime


# Get time zone offset from user
offset_hours = int(input("Enter the time zone offset to GMT in hours (e.g., +5 or -3): "))
offset = datetime.timedelta(hours=offset_hours)


# Display current time in GMT and specified time zone
current_time = datetime.utcnow()
timezone_time = current_time + offset

print(f"Current GMT time: {current_time}")
print(f"Time in specified time zone: {timezone_time}")