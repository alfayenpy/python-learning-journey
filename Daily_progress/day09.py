# Python String Methods

# Capitalize()

'''Makes the first character uppercase and everything lowercase'''

name = "alfayen"
print(name.capitalize())


# Title()

'''Makes the first character of each new word uppercase and everything lowercase'''

name1 = "md alfayen mondal"
print(name1.title())


# Casefold()

'''It turns the whole string to lowercase'''

name2 = "Md Alfayen Mondal"
print(name2.casefold())


# Center()

'''Places the string in the center of a specified width.'''

print(name.center(30, "="))              #Python adds spaces on both sides to make the total width 20.

'''
30 total spaces needed
7 used by "alfayen"
23 remaining
11 left + 12 right
'''



# Count

'''Counts how many times a value appears in a string'''


var = "i_am_alfayen"

print(var.count("a"))



# Find()

''' Finds the position of a character or word.

    find() returns the first match only'''

var1 = "HelloWorld"

print(var1.find("Hell"))




# Startswith()


'''Checks if a specific string starts with a specific value'''

website = "https://google.com"

print(website.startswith("https"))




# Endswith()

'''Checks if a specific string ends with a specific value'''

file = "report.pdf"

print(file.endswith(".pdf"))





# isalnum()

'''One of the most useful validation methods
    
    Checks if a string contains only letters and numbers


    No space, No Symbol, No special characters'''





num = "newnumber321"

print(num.isalnum())




# isalpha()

'''Checks if a string contains only letters'''


name67 = "alfayen"

print(name67.isalpha())




# isdigit()

'''Checks if a string contains only numbers'''


digit = "8972101894"

print(digit.isdigit())





# Join()

'''Join Multiple strings together'''


std = ["md", "alfayen", "mondal"]

print(" ".join(std))





# index()

'''Similar as find()
    
    this returns Value error if value not found'''



txt = "alfayen"

print(txt.index("a"))






