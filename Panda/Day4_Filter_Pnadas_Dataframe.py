# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# display dataframe
# print(dataFrame)


# Filter Pandas Dataframe with multiple conditions Using loc
# -->Here we will get all rows having Salary greater or equal to 100000 and Age < 40 and their JOB starts with ‘D’ from the dataframe. Print the details with Name and their JOB.

# filter dataframe
df_1 = dataFrame.loc[ (dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & (dataFrame['JOB'].str.startswith('D')) , ['Name','JOB']]
print(df_1)

# Filter Pandas Dataframe Using NumPy
import numpy as np 
np_2 =  np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & (dataFrame['JOB'].str.startswith('D')))
print(np_2)
print(dataFrame.loc[np_2])


# Filter Pandas Dataframe Using Query (eval and query works only with columns)
df_Q = dataFrame.query('Salary <= 100000 & Age < 40 & JOB.str.startswith("C").values')
print(df_Q)

# Eval multiple conditions  ("eval" and "query" works only with columns )
df_E = dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")]
print(df_E)

