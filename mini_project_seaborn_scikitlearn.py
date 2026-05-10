# customer_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# -----------------------------
# 1. Load Dataset
# -----------------------------
print("Loading dataset...")
df = pd.read_csv("customers-100.csv")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -----------------------------
# 2. Data Visualization
# -----------------------------
print("\nGenerating visualizations...")
print("Countries:\n",  df['Country'])
print("Country Value Counts:\n", df['Country'].value_counts())


# -----------------------------
# Top 10 countries by customer count
# -----------------------------
plt.figure(figsize=(10, 5))
top_countries = df['Country'].value_counts().head(10)
print("Top Countries Value Counts:\n", top_countries)

sns.barplot(x=top_countries.values, y=top_countries.index)

plt.title("Top 10 Countries by Customer Count")
plt.xlabel("Number of Customers")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("customer_distribution.png")  # Save chart
plt.show()

# -----------------------------
# 3. Convert to JSON
# -----------------------------
print("\nConverting dataset to JSON...")

json_data = df.to_json(orient="records", indent=2)

with open("customers.json", "w") as f:
    f.write(json_data)
print("JSON file saved as customers.json")

# -----------------------------
# 4. Machine Learning Model
# -----------------------------
print("\nRunning ML model (KMeans clustering)...")
df_ml = df.copy()

# Encode categorical columns safely - like Company, City,  Country
# This will be used  for cluster creation
label_encoders = {}
for col in df_ml.columns:
    if df_ml[col].dtype == 'object':
        le = LabelEncoder()
        df_ml[col] = le.fit_transform(df_ml[col].astype(str))
        label_encoders[col] = le

# Select numeric features only
X = df_ml.select_dtypes(include=['int64', 'float64'])

# Train KMeans - there will be 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df_ml['Cluster'] = kmeans.fit_predict(X)

print("\nClustered Data Sample:")
print(df_ml.head())

# -----------------------------
# 5. Visualize Clusters
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='Cluster', data=df_ml)

plt.title("Customer Segments (Clusters)")
plt.xlabel("Cluster")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.show()

# -----------------------------
# 6. Save Final Dataset
# -----------------------------
df_ml.to_csv("customers_with_clusters.csv", index=False)
print("\nSaved clustered dataset as customers_with_clusters.csv")

print("\n✅ Analysis Complete!")