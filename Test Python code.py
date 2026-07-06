dict = {}
arr = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

winner_vote = 0

for key,value in dict.items():
    if value > winner_vote:
        winner_vote = value

print(dict)
print(winner_vote)
winner_name = min(key for key,value in dict.items() if value == winner_vote)

print(winner_name)