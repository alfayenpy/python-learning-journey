# Python Match

# The match statement is used to perform different actions based on different conditions.

'''
Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed.



match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
'''



# Example :- Imagine you're making a game menu.
'''
1 → Start Game
2 → Settings
3 → Credits
4 → Exit
'''



choice = int(input("1.Start Game\n2.Settings\n3.Credits\n4.Exit\nEnter Your Choice :- "))

match choice:
    case 1:
        print("Start Game")

    case 2:
        print("Settings")

    case 3:
        print("Credits")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")









# Combine Values

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")




# If Statements as Guards

# You can add if statements in the case evaluation as an extra condition-check:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")






# Example :- 

name = input("Enter your name :- ")

match name.lower().endswith("mondal"):
    case True:
        print("You are from Mondal family")

    case False:
        print("You are not from Mondal family")






# CODE CHALLENGE

''' 

Inside the editor, complete the following steps:
Create a variable day with the value 3
Use a match statement to check the value of day
Add a case 3 that prints "Wednesday"
Add a wildcard case _ that prints "Other day"

'''






day = 3

match day:
    case 3:
        print("Wednesday")

    case _:
        print("Other day")