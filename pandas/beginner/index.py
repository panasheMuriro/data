import pandas as pd

# Create a Series from a list
s = pd.Series([10, 20, 30, 40])
print(s)

# Create a Series with custom indices
s_custom = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s_custom)

# Accessing by position
print(s[1])  # Output: 20

# Accessing by label
print(s_custom['b'])  # Output: 20

# Modifying values
s_custom['b'] = 25
print(s_custom)


data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)

data = [['Alice', 25, 'New York'], ['Bob', 30, 'San Francisco'], ['Charlie', 35, 'Los Angeles']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(data, columns=['Column1', 'Column2'])
print(df)

print(df.info())

print(df.describe()) 