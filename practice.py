import random

def get_class():

    firstnameclass = "aaron"

    class1 = ["Ferrari", "Lamborghini", "Aston Martin", "McLaren", "Bentley", "Porche"]
    class2 = ["Candle", "Toaster", "Golf Clubs", "Speaker", "Headphones", "Book"]

    if 1 < len(firstnameclass) <= 5:
        return class1
    else:
        return class2

print(get_class())


