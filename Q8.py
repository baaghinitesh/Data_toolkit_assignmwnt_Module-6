# 8. Perform the following tasks using people dataset:
# a) Read the 'data.csv' file using pandas, skipping the first 50 rows.
# b) Only read the columns: 'Last Name', 'Gender', 'Email', 'Phone' and 'Salary' from the file.
# c) Display the first 10 rows of the filtered dataset.
# d) Extract the 'Salary" column as a Series and display its last 5 values.

import pandas as pd

# a) Read the 'People Data.csv' file using pandas, skipping the first 50 rows
file_path = 'People Data.csv' 
df = pd.read_csv(file_path, skiprows=50)

df.columns = ['Index', 'Unique ID', 'First Name', 'Last Name', 'Gender', 
              'Email', 'Phone', 'DOB', 'Job Title', 'Salary']

# Check the first few rows to verify column names
print("\nFirst 10 rows of the entire dataset:")
print(df.head(10))

# b) Only read the specified columns
filtered_df = df[['Last Name', 'Gender', 'Email', 'Phone', 'Salary']]

# c) Display the first 10 rows of the filtered dataset
print("\nFirst 10 rows of the filtered dataset:")
print(filtered_df.head(10))

# d) Extract the 'Salary' column as a Series and display its last 5 values
salary_series = filtered_df['Salary']
print("\nLast 5 values of the Salary column:")
print(salary_series.tail(5))

