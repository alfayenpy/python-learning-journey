# Python Shorthand If


'''If you have only one statement to execute, you can put it on the same line as the if statement.'''


# One-line if statement:

a = 5
b = 2
if a > b: print("a is greater than b")



# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B")



# You can also use a one-line if/else to choose a value and assign it to a variable:


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)






'''variable = value_if_true if condition else value_if_false'''




# Multiple Conditions on One Line


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



