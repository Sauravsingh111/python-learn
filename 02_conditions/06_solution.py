# 6) Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 3

if distance < 3:
    print("Walk")
# elif distance >= 3 and distance <= 15:
elif distance <= 15:
    print("Bike")
else:
    print("Car")