# Python Dictionaries



''' Accessing Items


You can access the items of a dictionary by referring to its key name, inside square brackets:


'''




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(thisdict)






# get()


print(thisdict.get("model"))




# Get Keys

# The keys() method will return a list of all the keys in the dictionary.


x = thisdict.keys()





# Check If Key Exists


# To determine if a specified key is present in a dictionary use the in keyword:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



