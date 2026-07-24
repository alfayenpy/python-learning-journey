# Python For Loops

''' A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.





Syntax

for variable in collection:
    # code



'''


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


print()


# Looping Through a String


# Loop through the letters in the word "banana":

for x in "banana":
  print(x)






# The break Statement

# Exit the loop when x is "banana":


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


print()


# The continue Statement

# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)




print()


# The range() Function

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.




for x in range(6):
  print(x)




print()


# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):


# Increment the sequence with 3 (default is 1):



for x in range(2, 30, 3):
  print(x)





print()

# Else in For Loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:



for x in range(6):
  print(x)
else:
  print("Finally finished!")











# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)








# The pass Statement


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

















# CODE CHALLENGE

'''

Inside the editor, complete the following steps:
Create a list called fruits with: "apple", "banana", "cherry"
Write a for loop that prints each item in fruits
Use break to stop the loop when the item is "banana"

'''



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break
