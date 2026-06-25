# ***Iterating over rows and columns***

# 1. Iterating Over Rows
# There are several ways to iterate over the rows of a Pandas DataFrame and three common methods are:

# iteritems()
# iterrows()
# itertuples()

import pandas as pd
  
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}
 

# df = pd.DataFrame(dict)
# for i,j in df.iterrows():
#     print(i,j ,"\n")
    
# print(df)

#############################################################################
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}
 
# df = pd.DataFrame(dict)
# high_salary = []
# for i,row in df.iterrows():
#     s = row["score"]
#     if s > 80:
#         high_salary.append((row['name'],int(s)))

# print(high_salary)

# for name,score in high_salary:
#     print(f"{name}|{score}")
#############################################################################

# 2. Iterating Over Columns

# data = pd.read_csv(r"C:\Users\milan.pansuriya\Downloads\nba.csv")

# for label,values in data.head(2).items():
#     print(f"Column: {label}")
#     print(values)
#     print()

#############################################################################

# Working with Missing Data

# # 1. Checking for Missing Values using isnull() and notnull()
# -->To check for missing values (NaN) we can use two useful functions:

# isnull(): It returns True for NaN (missing) values and False otherwise.
# notnull(): It returns the opposite, True for non-missing values and False for NaN values.

# import numpy as np
 
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}

# df = pd.DataFrame(dict)
 
# print(df.isnull())
# print(df.notnull())

# 2. Filling Missing Values using fillna(), replace() and interpolate()

# import numpy as np
 
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
# df = pd.DataFrame(dict)
 
# print(df.fillna(0))

# 3. Dropping Missing Values using dropna()
import numpy as np
 
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
df = pd.DataFrame(dict)
   
print(df)
print(df.dropna())