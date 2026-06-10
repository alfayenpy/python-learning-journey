# python Slicing

a = "HelloWorld"

print(a[0:5])   # from index 0 to 4

# Slice from the start to index 5

print(a[:5])    # from index 0 to 4

# Slice from index 0 to the end

print(a[0:])  # from index 0 to 9








# Negative Indexing


print(a[-5:])






print()




# Python Modify Strings




# Upper Case

x = "welcome"
print(x.upper())




# Lower Case

y = "HELLO"
print(y.lower())



print()

# Strip ( removes space from beginning and end from the word or sentence)

name = " lol "
print(name.strip())




# Replace Method

var = "alfayen"

print(var.replace("l", "r") .replace("r", "ru") .replace("ayen", "ine"))

print()

# Split method

var1 = "cat dog bear lol"

print(var1.split())





print()








# String Concatenation


first_string = "Hello"
second_string = "World"

concatenated_string = first_string + " " + second_string


print(concatenated_string)




print()

# Python - Format - Strings


# f-strings





price = 150/2
txt = f"This item is {price:.2f} dollars"
print(txt)









details = f"MD.ALFAYEN MONDAL \nAge: {21} years old\nLocation: Basirhat"


print(f"Name: {details}")
