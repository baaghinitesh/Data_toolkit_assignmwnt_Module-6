# 10. Create a 7*5 Dataframe in Pandas using a series generated from 35 random integers between 1 to 6?

import pandas as pd
import numpy as np

# Generate 35 random integers between 1 and 6
random_integers = np.random.randint(1, 7, size=35)

# Create a DataFrame from the random integers
df = pd.DataFrame(random_integers.reshape(7, 5), columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5'])

# Print the resulting DataFrame
print("\n7x5 DataFrame of random integers:")
print(df)
