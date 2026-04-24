# Commonly used dictionary methods
# Dictionary comprehension
# In method 



labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300, "Jagmohan":1000,"Rampyare":800}

# Get Method
print(labour_with_cost.get("Mahesh")) # it will return the value of the key "Mahesh"
print(labour_with_cost.get("Mahesh1")) # it will return None because key "Mahesh1" is not present in the dictionary

print(labour_with_cost["Mahesh"]) # it will return the value of the key "Mahesh"
print(labour_with_cost["Mahesh1"]) # it will give an error because key "Mahesh1" is not present in the dictionary

# In producation we will use get() method to get the value of the key because it will not give an error if the key is not present in the dictionary and it will return None instead of giving an error.

# Key and value functions
print(labour_with_cost.keys()) # it will return the keys of the dictionary
print(labour_with_cost.values()) # it will return the values of the dictionary

# itmes() Function
print(labour_with_cost.items()) # it will return the key and value of the dictionary in the form of tuple

# update() function
labour_with_cost.update({"manish": 700,"Ram": 800})
print(labour_with_cost)

# Below is another method to update the dictionary (some time we used below method to update the dictionary)
new_dict = {"mahish":700, "Ram":900}
final_dict = {**labour_with_cost, **new_dict}
print(final_dict)

# Pop method
print(labour_with_cost.pop("Mahesh")) # it will remove the key "Mahesh" from the dictionary and return the value of the key "Mahesh"
print(labour_with_cost)

# popitem() method
print(labour_with_cost.popitem()) # it will remove the last key and value from the dictionary and return the key and value in the form of tuple
print(labour_with_cost)


###########################################################################################################################
labour_with_cost ={"Ram":100,"Jagmohan":200,"Aryan":300,"Ramesh":400}

#Dictionary Comprihension
labour_with_cost = {key : labour_with_cost.get(key)+100 for key in labour_with_cost}
print(labour_with_cost)

labour_with_cost = {key : labour_with_cost.get(key)+100 if key!="Jagmohan" else labour_with_cost.get(key) for key in labour_with_cost}
print(labour_with_cost)

print(len(labour_with_cost))

###########################################################################################################################

#Dictionary use hash mapping so it is faster then list with [in] keywork
letter_count = {}
name = "Manas"

for char in name:
    if char in letter_count:
        letter_count[char] = letter_count[char] +1
    else:
        letter_count[char] = 1

print(letter_count)