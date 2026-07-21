# Python Logical Operators


'''Logical operators are used to combine conditional statements. Python has three logical operators:


and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true

'''


# The and Operator

# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")





# The or Operator

# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")




# The not Operator

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")



# Combining Multiple Operators

# Python evaluates not first, then and, then or.

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")













# Python Nested If

# You can have if statements inside if statements. This is called nested if statements.


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")




# Multiple Levels of Nesting


# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.



score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")





# Nested If vs Logical Operators


# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.


temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")











# Python Pass Statement


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.



a = 33
b = 200

if b > a:
  pass



# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.






'''
Q. Why Use pass?


The pass statement is useful in several situations:

> When you're creating code structure but haven't implemented the logic yet
> When a statement is required syntactically but no action is needed
> As a placeholder for future code during development
> In empty functions or classes that you plan to implement later

'''





# pass with Multiple Conditions


value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")










# Python If...Else Code Challenge



'''

Inside the editor, complete the following steps:
Create a variable age with the value 20
Write an if statement that prints "Child" if age is less than 13
Add an elif that prints "Teenager" if age is less than 18
Add an else that prints "Adult"

'''

age = 20


if age < 13:
  print("Child")
elif age < 18:
    print("Teenager")
else:
  print("Adult")

