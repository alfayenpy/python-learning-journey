# Python Dictionary Methods


'''

Method	Description


clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

'''






'''
CODE CHALLENGE


Inside the editor, complete the following steps:
Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
Print the value of the "model" key
Add a new key "color" with the value "red"
Remove the "brand" key using pop()
Print the dictionary
'''


car = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 2024
}

print(car["Model"])

car["color"] = "red"

car.pop("brand")

print(car)