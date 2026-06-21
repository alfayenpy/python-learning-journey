'''
Favorite Countries Manager

What it does

User enters 3 favorite countries.

Program:-

Stores them in a list
Prints the list
Shows first country
Shows last country
Converts all countries to uppercase

'''
country1 = str(input("Enter First Country name :- "))
country2 = str(input("Enter Second Country name :- "))
country3 = str(input("Enter Third Country name :- "))

countries = [country1, country2, country3]


print("Your Favourite Countries")

print(countries)

print()


'''
print("First Country :- ", country1)
print()
print("Second Country :- ", country2)
print()
print("Third Country :- ", country3)
'''

print(countries[0])
print()
print(countries[-1])


print()

print("Does Japan Exist ?")

print("Japan" in countries)

print()

print("All Countries in Uppercase")

print()

print(country1.upper())
print(country2.upper())
print(country3.upper())