# First mini project of my journey 

# This project will be based on whatever i have learnt through 7 days of python journey 

# After every 7 day of daily progress there will be an mini project of whatever i've learnt 



# Taking Input From User

name = str(input("Enter Name : "))

Age = int(input("Enter Age : "))

Location = str(input("Enter Location : "))

Hobby = str(input("Enter Hobby : "))

Goal = str(input("Enter Goal : "))

Course = str(input("Enter Course : "))

University = str(input("Enter University : "))



# Capitalize 


name = name.strip().capitalize()

Location = Location.strip().title()

Hobby = Hobby.strip().title()

Goal = Goal.strip().title()

Course = Course.strip().title()

University = University.strip().title()



# Math Used

Next_Year_Age = Age + 1




# F-String Used

All_details = f" Name : {name}\n Age : {Age}\n Location : {Location}\n Hobby : {Hobby}\n Goal : {Goal}\n Course : {Course}\n University : {University}\n Next Year Age : {Next_Year_Age}\n"






print("======================================")

print("       STUDENT INFORMATION CARD       ")

print("======================================")

print()

print(All_details)

print("======================================")