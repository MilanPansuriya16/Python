# ***Pandas DataFrame***

# A Pandas DataFrame is a two-dimensional table-like structure in Python where data is arranged in rows and columns. 
# It’s one of the most commonly used tools for handling data and makes it easy to organize, analyze and manipulate data. 
# It can store different types of data such as numbers, text and dates across its columns. The main parts of a DataFrame are:

# Data: Actual values in the table.
# Rows: Labels that identify each row.
# Columns: Labels that define each data category.

# 1. Creating DataFrame using a List

import pandas as pd

lst = ['Geeks','For','Geeks','is','portal','for','Geeks']

df = pd.DataFrame(lst)
print(df)

# 2. Creating DataFrame from dict of ndarray/lists

data = {'Milan': [93,90,91],'Dhruvin':[90,91,89],'Raj':[80,85,87],'Romil':[82,85,86]}

# print(data)
df = pd.DataFrame(data)
print(df)

######################################################################################################################

# Working With Rows and Columns in Pandas DataFrame
# -->We can perform basic operations on rows/columns like selecting, deleting, adding and renaming.

# 1. Column Selection
# -->In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
df = pd.DataFrame(data)
 
print(df[['Name','Age']])


# 2. Row Selection
# Pandas provide unique methods for selecting rows from a Data frame. DataFrame.loc[] method is used for label-based selection
    
data = pd.read_csv(r"C:\Users\milan.pansuriya\Downloads\nba.csv", index_col="Name")
# print(data.head())          # Fetch and Print First 10 record by default
# print(data.head(10))        # Fetch and Print First 10 record by default
# print(data.tail())          # Fetch and Print Last 5 record by default 
# print(data.tail(10))        # Fetch and Print Last 10 record by default

# DataFrame.loc[] method is used for label-based selection, it is only work on the index column
first = data.loc[["Avery Bradley","R.J. Hunter"]]
second = data.loc["R.J. Hunter"]
 
print(first, "\n\n\n", second)

######################################################################################################################

# ***Indexing and Selecting Data in Pandas DataFrame***

# 1. Indexing a Dataframe using indexing operator []
# -->The indexing operator [] is the basic way to select data in Pandas. We can use this operator to access columns from a DataFrame.

data = pd.read_csv(r"C:\Users\milan.pansuriya\Downloads\nba.csv", index_col="Name")
first = data["Age"]
print(first)

# 2. Indexing a DataFrame using .loc[ ]
# -->The .loc method is used to select data by label.

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second)

# 3. Indexing a DataFrame using .iloc[ ]
# -->The .iloc() method allows us to select data based on integer position.

row2 = data.iloc[3] 
print(row2)