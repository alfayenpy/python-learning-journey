# Python *args and **kwargs




# *args



# Sometimes you don't know how many values the user will give.



'''
Syntax


def function_name(*args):
    # code

'''



def fun(*names):
    print(names)

fun("Alfayen", "Rahul", "Ayan")




'''

*args

↓

Collects multiple POSITIONAL arguments

↓

Stores them in a tuple.

'''











# **kwargs



# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.




'''
Syntax


def function_name(**kwargs):
    # code

'''





def student(**details):
    print(details)

student(name="Alfayen", age=20, country="India")






'''
*args

↓

Tuple ()

-------------------

**kwargs

↓

Dictionary {}












| `*args`                       | `**kwargs`                             |
| ----------------------------- | -------------------------------------- |
| Collects positional arguments | Collects keyword arguments             |
| Stores them in a tuple `()`   | Stores them in a dictionary `{}`       |
| Access by index               | Access by key                          |
| Example: `fun(10,20,30)`      | Example: `fun(name="Alfayen", age=20)` |



'''
