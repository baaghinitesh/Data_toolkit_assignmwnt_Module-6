# 7. Clean and transform the 'Phone' column in the sample dataset to remove non-numeric characters and convert it to a numeric data type. Also display the table attributes and data types of each column.

import pandas as pd

# Load the dataset
file_path = 'People Data.csv'
df = pd.read_csv(file_path)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Clean and transform the 'Phone' column
df['Phone'] = df['Phone'].replace(r'\D+', '', regex=True)

# Handle NaN values (e.g., fill with 0 or drop)
df['Phone'] = df['Phone'].fillna(0).astype(int)

# Display the transformed DataFrame
print("\nTransformed DataFrame:")
print(df)

# Display the DataFrame attributes and data types of each column
print("\nDataFrame Attributes:")
print(df.info())
