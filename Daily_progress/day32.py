# Python Dictionaries

# A Dictionary stores data in key : value pairs.


'''
Syntax for Dictionaries :-


{
key : value
}

'''

Student = {
    "name" : "alfayen",
    "Type" : "student",
    "age" : 21
}


print(Student)




# Dictionary items are ordered, changeable, and do not allow duplicates.




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print(len(thisdict))






thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}






# dict constructor


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)