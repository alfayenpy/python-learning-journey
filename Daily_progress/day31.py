# Code Challenge

'''

Inside the editor, complete the following steps:


Create a set called colors with the values "red", "green", "blue"
Print the set
Add "yellow" to the set using add()
Remove "green" from the set using discard()
Print the number of items using len()

'''



colors = {"red", "green", "blue"}

print(colors)

colors.add("yellow")

colors.discard("green")

print(len(colors))



print()






# Self Challenge



'''
animals = {"cat", "dog"}

# Add "lion"
# Add "tiger"
# Remove "cat"
# Print the set
# Print the length
'''



animals = {"cat", "dog"}

animals.update(["lion", "tiger"])

animals.remove("cat")

print(animals)

print(len(animals))

