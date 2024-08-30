# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "banana", "mango"]

# unique_item = set()

# for i in items:
#     if i in unique_item:
#         print("Duplicate", i)
#         break

#     unique_item.add(i)


unique_items = set()
duplicates = set()

for i in items:
    if i in unique_items:
        duplicates.add(i)
    else:
        unique_items.add(i)

if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("All items are unique")