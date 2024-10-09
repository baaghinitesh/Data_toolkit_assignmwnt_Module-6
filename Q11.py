# 11. Create two different Series, each of length 50, with the following criteria: 
# a) The first Series should contain random numbers ranging from 10 to 50.
# b) The second Series should contain random numbers ranging from 100 to 1000.
# c) Create a DataFrame by joining these Series by column, and, change the names of the columns to 'coll', 'col2',etc.

import pandas as pd
import numpy as np

# a) Create the first Series with random numbers ranging from 10 to 50
series1 = pd.Series(np.random.randint(10, 51, size=50))

# b) Create the second Series with random numbers ranging from 100 to 1000
series2 = pd.Series(np.random.randint(100, 1001, size=50))

# c) Create a DataFrame by joining these Series by column
df = pd.DataFrame({
    'col1': series1,
    'col2': series2
})

# Print the resulting DataFrame
print("\nDataFrame with two Series:")
print(df)

