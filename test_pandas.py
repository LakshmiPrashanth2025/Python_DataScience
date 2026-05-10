import inspect

import pandas as pd
from pandas.core.interchange import dataframe, column

df = pd.read_csv('people-100.csv')

#print top 5 rows
print(df.head())

# inspect dataframe
print("Dataframe Info ", df.info())
print("Dataframe Describe: ",df.describe())
print("Dataframe Columns ",df.columns)

# select columns
print("Phone column", df['Phone'])
print("Email & Phone columns", df[ ['Phone', 'Email']] )


print( df[ df['Sex'] =='Female' ] )

print( "Ascending Order Sort", df.sort_values('First Name'))
print( "Descending Order Sort", df.sort_values('First Name', ascending=False))

# Group by Gender
print("Group by Sex Count: ", df.groupby('Sex').value_counts())

# Add column
df['country'] = 'India'
print(df.head())


#print missing values
print(df.isnull())

df=df.drop_duplicates()
print("After removing duplicates:", df)





