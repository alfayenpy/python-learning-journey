print("===================================")
print(" Student Club Registration System ")
print("===================================")

name = input("Enter your name :- ")

if name == "":
    print("Name cannot be empty!")

roll = input("Enter your roll number :- ")

if roll == "":
    print("roll cannot be empty!")

student_details = (name, roll)

clubs = []

total_clubs = int(input("How many clubs do you want to join? :- "))

for i in range(total_clubs):
    club = input(f"Enter Club {i+1} :- ")
    clubs.append(club)

unique_clubs = set(clubs)

print()

print("===================================")
print(" Registration Summary ")
print("===================================")

print("Student Details :", student_details)

print("Total Clubs Selected :", len(clubs))

print("Unique Clubs :", len(unique_clubs))

print()

print("Registered Clubs")

for club in unique_clubs:
    print("-", club)

print()

if len(unique_clubs) >= 3:
    print("Excellent! You joined many clubs.")
else:
    print("Good! You can always join more clubs later.")

print()

print("Thank you for registering!")
print("===================================")