# Python Function Arguments

# An argument is a value that you pass to a function.



'''


def function_name(parameter):
    # code

function_name(argument)


'''


# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.



def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")





# Parameters vs Arguments

'''
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
'''


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument






# Number of Arguments


# If your function expects 2 arguments, you must call it with exactly 2 arguments.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")





print()


# Default Parameter Values

# You can assign default values to parameters. If the function is called without an argument, it uses the default value:



def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")







# Keyword Arguments

# You can send arguments with the key = value syntax.


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")






# Positional Arguments

# When you call a function with arguments without using keywords, they are called positional arguments.


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")









# Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)








# Passing Different Data Types

# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).


def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)








# Return Values

# Functions can return values using the return statement:


def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)







# Returning Different Data Types


def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])







# Positional-Only Arguments

def my_function(name, /):
  print("Hello", name)

my_function("Emil")








# Keyword-Only Arguments


def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")





# Combining Positional-Only and Keyword-Only



def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


