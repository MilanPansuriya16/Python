#String in python is case sensitive
'''
Name = 'Milan Pansuriya'

#Iteration in string
for i in Name:
    print(i)

#String Slicing
print(Name[0:4])

print(Name.isalpha())

#String methods
print(Name.lower())                   #Convert to lowercase
print(Name.upper())                   #Convert to uppercase
print(Name.title())                   #Convert to title case
print(Name.capitalize())              #Capitalize the first letter
print(Name.count('a'))                #Count the number of occurrences of 'a'
print(Name.find('P'))                 #To find the position of 'P', if character not found it give -1 and not give error
print(Name.index('P'))                #To find the position of 'P', if character not found it give error
print(Name.replace('Milan', 'John'))  #Replace 'Milan' with 'John'
print(Name.split(' '))                #Split the string by space
print(Name.split('a'))                #Split the string by 'a'
print(Name.strip())                   #Remove leading and trailing whitespace
print(Name.startswith('Milan'))       #Check if the string starts with 'Milan' , Returns true and false value
print(Name.endswith('Pansuriya'))     #Check if the string ends with 'Pansuriya', Returns true and false value
print(Name.isalpha())                 #Check if the string contains only alphabetic characters , Returns true and false value
print(Name.isalnum())                 #Check if the string contains only alphanumeric characters , Returns true and false value
print(Name.isdigit())                 #Check if the string contains only digits , Returns true and false value
print(ord('a'))                       #Get the Unicode code point of 'a', ASCII value is 97, it give ascii value
print(chr(97))                        #Get the character corresponding to the Unicode code point 97, it give 'a'
print(Name.swapcase())                #Swap case of the string, it convert uppercase to lowercase and lowercase to uppercase

'''

'''
Q1. Swap the case of the string without using swapcase 
inbuilt method for string

Input:- Programming Aasan Hai
Output:- pROGRAMMING aASAN hAI 
'''

'''
Q2. Print the list of all unique ip addresses?

Input:- 
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]

Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
           "10.168.155.22","10.168.167.2",
           "10.168.179.28","10.168.155.31" ]
'''
paths = """/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
    "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
    "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"""
print(paths)
print(len(paths))

new_paths = paths.split("/")
#print(new_paths)

unique_ips = set()
All_ips = []

for i in new_paths:
    if i.startswith("10."):
        unique_ips.add(i)
        All_ips.append(i)
    
print(unique_ips)
print(All_ips)

