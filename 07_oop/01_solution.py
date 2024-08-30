# OOP - Ek form lo bank ka vo class hogaya usme users form  bhar rahe he apna details ke sath vo object ho gaya

# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# attributes means nothing it says variable only
# instance means nothing ek form lo usme ek user ko bharna he

class Car:
    # def __init__(self, userbrand, usermodel): # __init__ isme kuch khas nahi he jese simple function ka name likhte he same vesa hi he bas __ lagaya he
        # self.brand = userbrand
        # self.model = usermodel
        # javascript me jo this he vo idhar self he exactly same kam
        # self matlab jisne bhi call kiya
        # jese idhar my_car ne call kiya to ye sabse pehle access lega uska

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand, my_new_car.model)

# to ye apne car ka form bana liye he aur niche brand aur model dalkar usko fill kiya ja raha he 

# __init__ ko constructor bhi kaha jata he
# Constructor vo method he jaha se object banta he kisi bhi class se to sabse pehle ye method call ho jata he
