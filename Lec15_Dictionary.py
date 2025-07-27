labour_with_cost ={"Ram":100,"Jagmohan":200,"Aryan":300,"Ramesh":400}

#Dictionary Comprihension
labour_with_cost = {key : labour_with_cost.get(key)+100 for key in labour_with_cost}
print(labour_with_cost)

labour_with_cost = {key : labour_with_cost.get(key)+100 if key!="Jagmohan" else labour_with_cost.get(key) for key in labour_with_cost}
print(labour_with_cost)

print(len(labour_with_cost))
############################################33
#Dictionary use hash mapping so it is faster then list with [in] keywork
letter_count = {}
name = "Manas"

for char in name:
    if char in letter_count:
        letter_count[char] = letter_count[char] +1
    else:
        letter_count[char] = 1

print(letter_count)