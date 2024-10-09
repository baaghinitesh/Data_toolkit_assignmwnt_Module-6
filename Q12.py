# 12. Perform the following operations using people data set:
# a) Delete the 'Email', 'Phone', and 'Date of birth' columns from the dataset.
# b) Delete the rows containing any missing values.
# d) Print the final output also.


import pandas as pd

# Read the 'People Data.csv' file using pandas, skipping the first 50 rows
file_path = 'People Data.csv'  # Ensure this path is correct
df = pd.read_csv(file_path, skiprows=50)

# Set the column names based on your previous structure
df.columns = ['Index', 'Unique ID', 'First Name', 'Last Name', 'Gender', 
              'Email', 'Phone', 'DOB', 'Job Title', 'Salary']

# a) Delete the 'Email', 'Phone', and 'DOB' columns from the dataset
df.drop(columns=['Email', 'Phone', 'DOB'], inplace=True)

# b) Delete the rows containing any missing values
df.dropna(inplace=True)

# d) Print the final output
print("\nFinal output after operations:")
print(df)
