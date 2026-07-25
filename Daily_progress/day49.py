# Python Functions


'''
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.
'''





# Creating a Function


# In Python, a function is defined using the def keyword, followed by a function name and parentheses:



def my_function():
    abc = int(input("Enter a number :- "))
    for i in range(1, abc + 1):
        print("*" * i)








# Calling a Function

# To call a function, write its name followed by parentheses:


my_function()









# Function Names

'''
Function names follow the same rules as variable names in Python:


> A function name must start with a letter or underscore
> A function name can only contain letters, numbers, and underscores
> Function names are case-sensitive (myFunction and myfunction are different)
'''





# Why Use Functions?

'''
Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:
'''






# Return Values


'''
Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:
'''



def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)




# The pass Statement

def my_function():
  pass
