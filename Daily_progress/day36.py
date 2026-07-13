# Python - Remove Dictionary Items





# pop()

# The pop() method removes the item with the specified key name:



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)











# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)









# del()

# The del keyword removes the item with the specified key name:

# The del keyword can also delete the dictionary completely:



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]   # To remove the whole dict then remove the specified value
print(thisdict)










# clear()


# The clear() method empties the dictionary:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)