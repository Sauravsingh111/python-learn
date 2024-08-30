# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:

    x = int(input())

    if 1 <= x <= 10:
        print("Thanks")
        break

    else:
        print("Invalid Number")