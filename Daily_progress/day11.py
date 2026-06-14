# Python Operators


# Arithmetic Operation

'''
Addition
Substraction
Multiplication
Division
Modulus
Exponent
Floor Division
'''



print(15+22) # Addition

print(66-59) # Substraction

print(25*5) # Multiplication

print(69/33) # Returns a Float value

print(55%5) # Returns remainder

print(5**3) # Power

print(56//5) # Removes decimal part.




print()



# Assignment Operators


'''

=
+=
-=
*=
/=

'''





x = 10

x += 5
print(x)



x = 10

x -= 5
print(x)



x = 10

x *= 5
print(x)



x = 10

x /= 5
print(x)







# Ternary Operator


'''

    value_if_true if condition else value_if_false

'''


age = int(input("Enter Age : "))

print("You are not able to vote" if age >= 18 else "You are able to vote")








# Comparison Operators



# Equal to (==)  :- Used to check if the value is equal


num = 10

print(num==10)



# Not Equal to (!=) :- Checks if the value is not equal 


print(num != 100)



# Greater than  &  Less than

print(num > 30)

print(num < 520)



# Greater than Equal to , Less than Equal to  ( <= , >= )


print(num <= 100)

print(num >= 10)









# Logical Operators



#   and , or , not





# AND operator      :-      Both conditions must be true otherwise False



print(5!=2 and 10>2)



# OR operator       :-      Atleast one condition must be true otherwise False



print(30 == 50 or 20 >= 2)




# Not operator      :-      Reverses the answer


print(not True)