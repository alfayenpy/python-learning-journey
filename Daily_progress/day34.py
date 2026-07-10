# Python Change Dictionary Items




# Change a Value Using the Key


student = {
    "name" : "alfayen",
    "age" : "21",
    "course" : "BCA",
    "country" : "India"
}

student["country"] = "Japan"

print(student)







# update()


student = {
    "name": "Alfayen",
    "age": 20
}

student.update({"age": 21})

print(student)





# updating Multiple Values


student = {
    "name": "Alfayen",
    "age": 20,
    "country": "India"
}

student.update({
    "age": 21,
    "country": "Japan"
})

print(student)

