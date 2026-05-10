import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


df = pd.read_csv('people-100.csv')
print(df.head())

df['Date of birth']=pd.to_datetime(df['Date of birth'])

current_year = datetime.now().year
df['Age']=current_year - pd.to_datetime(df['Date of birth']).dt.year

print(df[['Date of birth', 'Age']]. head())



df['Sex_Number'] = df['Sex'].map({'Male':0, 'Female':1})
X = df[['Sex_Number']]
Y = df['Age']

print(df[['Sex_Number', 'Age']]. head())

model=LinearRegression()
model.fit(X, Y)

#predict=1 means
print("The predicted Average Age of Female" ,  model.predict([[1]]))