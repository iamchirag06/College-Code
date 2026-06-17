import numpy as np

data = [4, 8, 6, 5, 3]
var_pop = np.var(data)          # Population variance (ddof=0)
var_sample = np.var(data, ddof=1) # Sample variance
print(f"Population variance: {var_pop}")   # 2.96
print(f"Sample variance: {var_sample}")     # 3.7