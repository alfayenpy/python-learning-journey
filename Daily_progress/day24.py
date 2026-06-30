# Update Tuples


#   Convert → Modify → Convert Back.


countries = ("korea", "india", "brazil")

countries = list(countries)

countries.pop(1)

countries = tuple(countries)

print(countries)






# Unpack Tuples


'''Number of variables = Number of tuple items'''

cars = ("audi", "bmw", "lamborghini", "merceedez")

car1, car2, car3, car4 = (cars)


print(car1)
print(car2)
print(car3)
print(car4)
