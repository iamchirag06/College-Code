import numpy as np 
 
original = np.array([10, 20, 30, 40, 50]) 
 
# Creating a view via slicing 
my_view = original[1:4]  # [20, 30, 40] 
 
# Modifying the view 
my_view[0] = 99 
 
# The original array changes too! 
print("Original:", original)  # Output: [10, 99, 30, 40, 50] 
print("View:", my_view)        # Output: [99, 30, 40] 