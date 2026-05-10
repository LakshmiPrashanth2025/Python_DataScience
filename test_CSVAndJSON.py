import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
import json

#CSV to JSON

df = pd.read_csv('people-100.csv')
print(df.head())

df_small_dataset= df[['First Name','Last Name','Email']]

json_data = df_small_dataset.to_json(orient='records')
print("The CSV converted to JSON String is ",json_data)

json_data1 = { "name":"Jason",
              "age":25,
              "city":"New York"}
json_str = json.dumps(json_data1)
print("The JSON String is ", json_str)

# JSON to CSV

json_data_list = [
                { "name":"Jason", "age":25, "city":"New York"},
                { "name":"Alice", "age":35, "city":"London"},
                { "name":"Bob", "age":15, "city":"Melbourne"}]
df2=pd.DataFrame(json_data_list)
print("The JSON List converted to CSV tabulation " , df2.head())




