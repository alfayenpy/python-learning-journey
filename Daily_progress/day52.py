# Python Scope

# A variable is only available from inside the region it is created. This is called scope.



'''
Local Variable

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
'''


def myfunc():
  x = 300
  print(x)

myfunc()


print()





# Function Inside Function


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()






# Global Scope


x = 300

def myfunc():
  print(x)

myfunc()

print(x)










print()




x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)