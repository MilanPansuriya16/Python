from loguru import logger


# find the count of the world 'the' in the paragraph
paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the first commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """

paragraph_list = paragraph.lower().split(" ")

# print(paragraph_list)
count = 0
for letter in paragraph_list:
    if letter == "the":
        count = count + 1
    
logger.info(f"the count of the world 'the' in the paragraph is {count}")

# I have a sorted list and need to insert the new value in such a way that after inserting the new element list will be sorted.
# list = [5,18,77,108,930]
# number_to_insert = 100

list1 = [5,18,77,108,930]
number_to_insert = 100
index_of_insertion = 0

for number in list1:
    if number < number_to_insert:
        index_of_insertion = index_of_insertion + 1
    else:
        index_of_insertion = index_of_insertion
        break
# print(index_of_insertion)

list1.append('')	
for i in range(len(list1)-1,index_of_insertion,-1):
	list1[i] = list1[i-1]

list1[index_of_insertion] = number_to_insert

print(list1)
