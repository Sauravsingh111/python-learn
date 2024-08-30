# 1) Age group categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = 19

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenage")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior") 