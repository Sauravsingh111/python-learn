# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

s = "aabcd"

for char in s:
    if s.count(char) == 1:
        print("Char is:", char)
        break
    