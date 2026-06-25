# ***Iterating over rows and columns***

# 1. Iterating Over Rows
# There are several ways to iterate over the rows of a Pandas DataFrame and three common methods are:

# iteritems()
# iterrows()
# itertuples()

import pandas as pd
  
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 

df = pd.DataFrame(dict)
# for i,j in df.iterrows():
#     print(i,j ,"\n")
    
# print(df)

# 2. Iterating Over Columns
high_salary = []
for i,row in df.iterrows():
    s = row["score"]
    if s > 80:
        high_salary.append((row['name'],int(s)))

print(high_salary)

for name,score in high_salary:
    print(f"{name}|{score}")
          
