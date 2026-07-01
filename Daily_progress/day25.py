# Loop Tuples


# For Method

'''countries = ("Sydney", "Korea", "India", "")

for country in countries:
    print(country)
'''


countries = ("India", "Japan", "Canada")

for i in range(len(countries)):
    print(countries[i])





# Join Tuples

'''Combine two tuples into one tuple.'''


tuple1 = ("India", "Japan")

tuple2 = ("Canada", "Korea")

joined_tuple = tuple1 + tuple2

print(joined_tuple)

print()

tuple1 = ("car",)

tuple2 = ("bike",)

tuple3 = tuple1 + tuple2
print(tuple3)






# Repeat Tuple Using *


tuple1 = ("car",)

print(tuple1 * 2)



# Multiply Tuples


tuple67 = ("67", "98", "01")

lol = tuple67 * 2

print(lol)






# Tuple Methods 


# Count Method 


method = ("cars", "bikes", "vehicle")

print(method.count("cars"))


# Index Method


method00 = ("singer", "dancer", "coder")

print(method00.index("coder"))



# Duplicate Value Method


countries = ("India", "Japan", "India", "Canada")

print(countries.index("India"))











# Code Challenge


'''Inside the editor, complete the following steps:
Create a tuple called fruits with the values "apple", "banana", "cherry"
Print the second item in the tuple
Print the number of items using len()
Unpack the tuple into three variables a, b, c
Print the variable b'''


fruits = ("apple", "banana", "cherry")

print(fruits[1])

print(len(fruits))

a, b, c = fruits

print(b)

