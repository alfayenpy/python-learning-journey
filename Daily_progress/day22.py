# List Methods

'''
| Method    | Purpose            | Learned |
| --------- | ------------------ | :-----: |
| append()  | Add one item       |    ✅    |
| insert()  | Add at index       |    ✅    |
| remove()  | Remove by value    |    ✅    |
| pop()     | Remove by index    |    ✅    |
| clear()   | Remove all items   |    ❌    |
| copy()    | Copy list          |    ✅    |
| sort()    | Sort ascending     |    ✅    |
| reverse() | Reverse list order |    ❌    |
| extend()  | Join lists         |    ✅    |
| count()   | Count occurrences  |    ❌    |
| index()   | Find position      |    ❌    |

'''


# The Remaining Ones


list1 = ["apple", "banana", "Guava"]
list1.clear()
print(list1)



list1 = ["apple", "banana", "Guava"]
list1.reverse()
print(list1)




ez = list1.count("banana")
print(ez)


for fruits in list1:
    if("nana") in fruits:
        print(fruits)




countries = ["India", "Japan", "Canada"]

print(countries.index("Japan"))




# Code Challenge

'''
Inside the editor, complete the following steps:
Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list using append()
Remove "red" from the list using remove()
Print the list
'''



colors = ["red", "green", "blue"]

print(colors[0])

colors[1] = "yellow"

colors.append("purple")

colors.remove("red")

print(colors)
