#String in python is case sensitive

Name = 'Milan Pansuriya'

#Iteration in string
for i in Name:
    print(i)

#String Slicing
print(Name[0:4])

print(Name.isalpha())

#String methods
print(Name.lower())         #Convert to lowercase
print(Name.upper())         #Convert to uppercase
print(Name.title())         #Convert to title case
print(Name.capitalize())    #Capitalize the first letter
print(Name.count('a'))      #Count the number of occurrences of 'a'
print(Name.find('P'))       #To find the position of 'P', if character not found it give -1 and not give error
print(Name.index('P'))      #To find the position of 'P', if character not found it give error
print(Name.replace('Milan', 'John'))  #Replace 'Milan' with 'John'
print(Name.split(' '))      #Split the string by space
print(Name.split('a'))      #Split the string by 'a'
print(Name.strip())        #Remove leading and trailing whitespace
print(Name.startswith('Milan'))  #Check if the string starts with 'Milan' , Returns true and false value
print(Name.endswith('Pansuriya'))  #Check if the string ends with 'Pansuriya', Returns true and false value
print(Name.isalpha())      #Check if the string contains only alphabetic characters , Returns true and false value
print(Name.isalnum())      #Check if the string contains only alphanumeric characters , Returns true and false value
print(Name.isdigit())      #Check if the string contains only digits , Returns true and false value
print(ord('a'))            #Get the Unicode code point of 'a', ASCII value is 97, it give ascii value
print(chr(97))             #Get the character corresponding to the Unicode code point 97, it give 'a'

