# Python Loop Sets

# for loop

maths = {"addition", "substraction", "multiplication", "division"}

for math in maths:
    print(math, end=", ")





# Using len() with a set


countries = {"India", "Japan", "Canada"}

print(len(countries))









# Python Join Lists


# union() =  creates a new set by combining two sets.



set1 = {"apple", "banana"}

set2 = {"guava", "litchi"}


set3 = set1.union(set2)

print(set3)






# update()


lol = {"apple"}

lol.update({"banana"})

print(lol)






# intersection() = Keep only the common (duplicate) items.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple", "microsoft"}

print(set1.intersection(set2))







# difference() = Keep items from the first set only.



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple"}

print(set1.difference(set2))







# symmetric_difference() = Keep items that are NOT common.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple"}

print(set1.symmetric_difference(set2))
