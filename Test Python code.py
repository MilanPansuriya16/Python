s = 'geEksforGEeks'
dict = {}
	    
for i in s:
    if i in dict:
        continue
    else:
        dict[i] = 1
   
print(dict)
    