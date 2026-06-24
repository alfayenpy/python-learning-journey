# List Comprehension


'''
List Comprehension is a shorter way to create a new List.
'''



# Example :-

countries = ["Japan", "Tokyo", "Kyoto"]



new_countries = [country for country in countries]
print(new_countries)



names = ["Alfayen", "Japan", "Python"]

new_names = [name for name in names]

print(new_names)




# Suppose u want a specific country only with letter a then :


countries = ["Japan", "Tokyo", "Kyoto"]

new_countries = [country for country in countries if "a" in country]

print(new_countries)
