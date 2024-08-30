# 10) Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

pet = "cat"
age = 8

# if (pet == "dog") and (age >= 2):
#     print("Dog Food")
# elif (pet == "dog") and (age < 2):
#     print("Puppy Food")
# elif (pet == "cat") and (age > 5):
#     print("Senior Cat Food")
# elif (pet == "cat") and (age <= 5):
#     print("Junior Cat Food")
# else:
#     print("No data for", pet)

if pet == "dog":
    if age > 2:
        print("Dog Food")
    elif age <= 2:
        print("Puppy Food")

elif pet == "cat":
    if age > 5:
        print("Senior Cat Food")
    elif age <= 5:
        print("Junior Cat Food")

else :
    print("No data for", pet)