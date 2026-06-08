
s = 'testsample'
list = [0] * 26
        
for i in range(len(s)):
    list[ord(s[i])-97] += 1
    

max_frq = max(list)

for i in range(26):
    if max_frq == list[i]:
        print(chr(i+97))