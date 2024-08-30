# 4) Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color != "Green" and color != "Yellow" and color!= "Brown":
        print("Enter valid color")
        exit()

    if color == "Green":
        print(fruit, "- Unripe")
    elif color == "Yellow":
        print(fruit, "- Ripe")
    elif color == "Brown":
        print(fruit, "- Overripe")

else:
    print("No information about", fruit)