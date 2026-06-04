# beg_index = k+1
# end_index = k
        
# arr[beg_index],arr[end_index] = arr[beg_index],arr[-end_index]
s = "i love programming"    
new_s = s.split(' ')
for i in range(len(new_s)):
    char = new_s[i]
    word = char[0].upper()
    new_word = word + char[1:]
    new_s[i] = new_word

output = ' '.join(new_s)
print(output)