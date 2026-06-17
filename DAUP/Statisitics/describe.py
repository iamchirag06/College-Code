import pandas as pd
import numpy as np

# Sample dataset of real estate properties
data = {
    'Price': [350000, 420000, 290000, 850000, 310000, 410000],
    'Beds': [3, 4, 2, 5, 3, 3],
    'Square_Feet': [1800, 2200, 1200, 4500, 1500, 2100]
}
df = pd.DataFrame(data)

# Generate standard descriptive summary
print(df.describe())
print(df.mean())