from loguru import logger

logger.info("Programming Aasan he")


# Using for loop
Even_list = []
Odd_list = []
for i in range(1,11):
    if i%2==0:
        Even_list.append(i)
    else:
        Odd_list.append(i)

print(Even_list)
print(Odd_list)

# Using List comprehension
Even_list = []
Odd_list = []


Even_list = [i for i in range(1,11) if i%2==0]
print(Even_list)

Odd_list = [i for i in range(1,11) if i%2!=0]
print(Odd_list)


####################################################################################################################

from loguru import logger

# logger.info(f'Hii , My self Milan Pansuriya your python tutorial helper')

Paragraph = "A paragraph is a distinct unit of writing, typically composed of multiple sentences, that focuses on a single idea or topic. It serves as a building block for longer pieces of text, helping to organize and structure information for the reader. Paragraphs usually begin with an indentation and consist of a topic sentence, supporting sentences, and sometimes a concluding sentence."
Paragrah_list = Paragraph.lower().split(' ')

print(Paragrah_list)
count = 0
Search_word = 'for'
for i in Paragrah_list:
    if i == Search_word:
        count = count + 1
    else:   
        continue

print(count)
