# Python - Copy Dictionaries





# cop()

# Make a copy of a dictionary with the copy() method:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)





# dict()
# Another way to make a copy is to use the built-in function dict().


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)