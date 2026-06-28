# Project 03 - Travel Planner

print("===================================")
print("          Travel Planner")
print("===================================")

name = input("Enter Name :- ")
favourite_country = input("Enter Favourite Country :- ")
total_budget = int(input("Enter the Budget :- "))

if total_budget <= 150000:
    budget_type = "Low Budget"
elif total_budget <= 250000:
    budget_type = "Average Budget"
elif total_budget <= 1000000:
    budget_type = "Good Budget"
else:
    budget_type = "Luxury Budget"

wishlist = []

wishlist_places = int(input("How many places do you want to visit ? :- "))

for i in range(wishlist_places):
    place = input(f"Enter Place {i + 1} :- ")
    wishlist.append(place)

print()
print("===================================")
print("          Travel Planner Report")
print("===================================")

print()
print("----------- Traveller Details -----------")
print("Traveller Name :-", name)
print("Dream Country :-", favourite_country)
print("Budget :- ₹", total_budget)
print("Budget Type :-", budget_type)
print("----------------------------------------")

print()
print("----------- Wishlist -----------")

for place in wishlist:
    print("-", place)

print("--------------------------------")

print()
print("Total Places :-", len(wishlist))

print()
print("Thank you for using Travel Planner!")