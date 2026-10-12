import pandas as pd
import numpy as np

# Generate ten random numbers
random_numbers = np.random.randint(1, 100, 10)

# Create a Pandas Series
ser = pd.Series(random_numbers)

# Display the Series
print("Pandas Series with 10 Random Numbers:")
print(ser)
