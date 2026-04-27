# About Strings in Python
# Methods of String
# Slicing in String
# 2 Programming Questions on String


name = "Manish Kumar"
print(name)

# Scaling in string
print(name[0:5])


# Interation in String
for char in name:
    print(char)

# Methods of String 

print(name.lower())                   #Convert to lowercase
print(name.upper())                   #Convert to uppercase
print(name.title())                   #Convert to title case
print(name.capitalize())              # it will capitalize the first letter of the string and make all other letters in the string small
print(name.count('a'))                #Count the number of occurrences of 'a'
print(name.find('P'))                 #To find the position of 'P', if character not found it give -1 and not give error
print(name.index('P'))                #To find the position of 'P', if character not found it give error
print(name.replace('Milan', 'John'))  #Replace 'Milan' with 'John'
print(name.split(' '))                #Split the string by space
print(name.split('a'))                #Split the string by 'a'
print(name.strip())                   #f leading and trailing whitespace
print(name.startswith('Milan'))       #Check if the string starts with 'Milan' , Returns true and false value
print(name.endswith('Pansuriya'))     #Check if the string ends with 'Pansuriya', Returns true and false value
print(name.isalpha())                 #Check if the string contains only alphabetic characters , Returns true and false value
print(name.isalnum())                 #Check if the string contains only alphanumeric characters , Returns true and false value
print(name.isdigit())                 #Check if the string contains only digits , Returns true and false value
print(ord('a'))                       #Get the Unicode code point of 'a', ASCII value is 97, it give ascii value
print(chr(97))                        #Get the character corresponding to the Unicode code point 97, it give 'a'
print(name.swapcase())                #Swap case of the string, it convert uppercase to lowercase and lowercase to uppercase

##########################################################################################################################
# Question
# Find the name which ends with "h" from the given string and return the nane in the list

name = "Manish, Meet, Milan, Rohit, Ramesh"

name_list = name.split(",")
lst = []
for name in name_list:
    if name.endswith("h"):
        lst.append(name)
    else:
        print(f"{name} does not end with h")

##########################################################################################################################
# Hide the email address in the given string and return the string with hidden email address

email = "joan.doe@example.com"

email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

# print(username)
# print(domain)

hidden_username = ""
for i in range(len(username)):
    if i == 0 or i == len(username) - 1:
        hidden_username = hidden_username + username[i]
    else:
        hidden_username = hidden_username + "*"

hidden_email = hidden_username + "@" + domain

print(hidden_email)

##########################################################################################################################

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

# print(paths)
path_list = paths.split("/")
# print(path_list)

all_ips = []

for i in path_list:
    if i.startswith("10."):
        all_ips.append(i)

unique_ips = set(all_ips)
   
print(all_ips)
print(unique_ips)