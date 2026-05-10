import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('people-100.csv')
print(df.head())

sns.countplot(x='Sex', data=df)
plt.title("Gender Distribution")
plt.show()

sns.countplot(x='Job Title', data=df)
plt.title("Job Distribution")
plt.show()

plt.figure(figsize=(40,10))
sns.countplot(x='Job Title',hue='Sex', data=df)
plt.title("Job Distribution with Gender Hue")
#plt.xticks(rotation=45)
plt.xticks(rotation=45, fontsize=10)
plt.show()


