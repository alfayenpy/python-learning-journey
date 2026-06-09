# Python Strings


x = "Hello World"
y = 'Hello World'

# Quotes inside a quote


a = "It's a nice day"
b = 'She said "Hello"'




# Multiline Strings
c = """This is a multiline string
that spans multiple lines."""




print("\n")




# String are arrays

a = "Hello World"
print(a[0])  # H
print(a[1])  # e
print(a[2])  # l
print(a[3])  # l
print(a[4])  # o
print(a[5])  # (space)




# ()  -> Function Call
# []  -> Indexing / Slicing





# Looping through a string
for chart in a:
    print(chart)


# String Length
print(len(a))  # 11



 # Check String

txt = "The best things in life are free!"
print("free" in txt)  # True


txt = "The best things in life are free!"
print("expensive" not in txt)