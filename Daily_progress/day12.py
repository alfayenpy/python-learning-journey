# Identity Operators


'''
is
is not
'''




# Returns True if both variables are the same object


num1 = "lol"
num2 = "lol"


print(num1 is num2)



# Returns True if both variables are not the same object


num1 = "alfayen"
num2 = "mondal"


print(num1 is not num2)









# Membership Operator


'''
in
not in
'''



# Returns True if a sequence with the specified value is present in the object



a = "alfayen123"

print("a" in a)


print("32" not in a)











# Bitwise Operator


'''Bitwise works on the binary representation of numbers.'''




# Bitwise AND (&)                   



'''

1 & 1 = 1

Everything else = 0

'''


print(5 & 3)





# Bitwise OR (|)


'''

0 | 0 = 0

Everything else = 1

'''


print(5 | 3)






# Bitwise XOR (^)


'''

Same bits → 0
Different bits → 1

'''


print(5 ^ 3)








# Operator Preceedence


'''


1. ()
2. **
3. * / // %
4. + -
5. Comparison (==, !=, >, <)
6. not
7. and
8. or


'''








'''

Inside the editor, complete the following steps:
Create two variables a = 15 and b = 4
Print the result of a modulus b (the % operator)
Print the result of a floor division b (the // operator)
Print the result of a to the power of b (the ** operator)
Use an assignment operator to add 10 to a (use +=)

'''



a = 15
b = 4

print(a%b)
print(15//4)
print(15**4)
a+=10
print(a)

