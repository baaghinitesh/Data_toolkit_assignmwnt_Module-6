

import pandas as pd

file_path = 'People Data.csv' 
df = pd.read_csv(file_path, skiprows=50)

# Set the column names based on your previous structure
df.columns = ['Index', 'Unique ID', 'First Name', 'Last Name', 'Gender', 
              'Email', 'Phone', 'DOB', 'Job Title', 'Salary']

# Convert 'Salary' column to numeric, in case it's read as string
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Filter rows based on the specified conditions
filtered_rows = df[(df['Last Name'].str.contains('Duke', na=False)) & 
                   (df['Gender'] == 'Female') & 
                   (df['Salary'] < 85000)]

# Display the filtered rows
print("\nFiltered rows based on conditions:")
print(filtered_rows)
