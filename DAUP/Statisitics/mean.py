import numpy as np
import pandas as pd

data = [10, 20, 30, 40, 50]
mean_numpy = np.mean(data)
mean_pandas = pd.Series(data).mean()
print(f"Mean: {mean_numpy}")  # Output: 30.0