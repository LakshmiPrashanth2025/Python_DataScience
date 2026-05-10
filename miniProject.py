# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv('people-100.csv')

# Clean column names
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns)

# Rename column for consistency
df = df.rename(columns={'Sex': 'Gender'})

# 2. Create Salary column
np.random.seed(42)
df['Salary'] = np.random.randint(20000, 100000, size=len(df))

# 3. Add City column (Indian cities)
cities = ['Bangalore', 'Mumbai', 'Delhi', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata']
np.random.seed(42)
df['City'] = np.random.choice(cities, size=len(df))

# 4. Clean Gender column
df['Gender'] = df['Gender'].astype(str).str.strip().str.capitalize()

# 5. Salary Category (High > 60000, else Low)
df['Salary_Category'] = np.where(df['Salary'] > 60000, 'High', 'Low')

# 6. Analysis

# Gender count
gender_count = df['Gender'].value_counts()
print("\nGender Count:\n", gender_count)

# Average salary by gender
avg_salary_gender = df.groupby('Gender')['Salary'].mean()
print("\nAverage Salary by Gender:\n", avg_salary_gender)

# Average salary by city
avg_salary_city = df.groupby('City')['Salary'].mean()
print("\nAverage Salary by City:\n", avg_salary_city)

# ✅ Average salary by job title (retained)
avg_salary_job = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False)
print("\nAverage Salary by Job Title:\n", avg_salary_job.head())

# 7. Visualization

# Gender Distribution
gender_count.plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Average Salary by Gender
avg_salary_gender.plot(kind='bar', color=['blue', 'red'])
plt.title('Average Salary by Gender')
plt.ylabel('Salary')
plt.show()

# Average Salary by City
avg_salary_city.plot(kind='bar', color='green')
plt.title('Average Salary by City')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()

# ✅ Top 10 Job Titles by Salary
avg_salary_job.head(10).plot(kind='bar', color='teal')
plt.title('Top 10 Job Titles by Average Salary')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()

# Salary Distribution
plt.hist(df['Salary'], bins=10, color='blue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Salary Category Distribution
df['Salary_Category'].value_counts().plot(kind='bar', color=['blue', 'teal'])
plt.title('Salary Category Distribution')
plt.show()

# 8. Save Processed Data
df.to_csv('processed_people.csv', index=False)

print("\n✅ Process completed and saved as 'processed_people.csv'")