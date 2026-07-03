# Access Set Items

# Using a For loop

countries = {"kyoto", "japan", "india"}

for country in countries:
    print(country)


# Using a In Method = Checks whether the item exists or not

laps = {"lap1", "lap2", "lap3"}

print("lap2" in laps)







# Add Set Items = Used to Add one item.


# add()     -->     Adds one item

setss = {"num", "var", "char"}

setss.add("bool")

print(setss)    # If Item already exists then nothing changes everything remains same






# Update Method     =   update()    --> adds multiple items.


chart = {"numbers", "alphabets", "characters"}

chart.update(["cars", "bikes"])

print(chart)











# Remove Set Items


# remove()


countries = {"Japan", "India", "Canada"}

countries.remove("India")

print(countries)





# discard()

countries = {"Japan", "India", "Canada"}

countries.discard("Japan")

print(countries)




'''

remove()
❌ Error if item doesn't exist.

discard()
✅ No error if item doesn't exist.

'''

