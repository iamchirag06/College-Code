import numpy as np
arr = np.array([1, 2, 3, 4])
arr_copy = arr.copy()  # Copy creates a NEW array
arr_copy[0] = 100  # Modify the copy
print("Original Array:", arr)   # Original is unchanged
print("Copied Array:", arr_copy)  # Only the copy changes