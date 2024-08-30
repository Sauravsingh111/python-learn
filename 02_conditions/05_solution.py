# 5) Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = "Rainy"

adjust_weather = weather.lower()
print(adjust_weather)

if adjust_weather == "sunny":
    print("Weather -", weather, "(Go for a walk)")
elif adjust_weather == "rainy":
    print("Weather -", weather, "(Read a book)")
elif adjust_weather == "snowy":
    print("Weather -", weather, "(Build a snowman)")
else:
    print("No such weather exists in my database")