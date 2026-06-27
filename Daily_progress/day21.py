# Join Lists


'''
3 Types

+ Operator Method
append with a loop Method
extend Method
'''






list1 = ["Youtube", "Instagram", "Whatsapp"]

list2 = ["Chatgpt", "Claude", "Gemini"]

new_added_list = list1 + list2

print(new_added_list)


for item in list2:
    list1.append(item)


print(list1)




list1.extend(list2)

print(list1)

