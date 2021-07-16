import random

def get_class():

    firstnameclass = 'ben'

    car = random.choice(['Ferrari', 'Lamborghini', 'McLaren'])
    watch = random.choice(['Rolex', 'Audemars Piguet', 'Richard Mille'])

    if 1 < len(firstnameclass) < 5:
        return car
    else:
        return watch

print(get_class())