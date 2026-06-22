import numpy as np 
 
a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6]) 

arr= np.dstack((a,b))
print(arr)

matrix_a = np.array([[1, 2], [3, 4]]) 
matrix_b = np.array([[5, 6], [7, 8]]) 
 
# Concatenate along rows (Axis 0) - same as vstack 
print(np.concatenate((matrix_a, matrix_b), axis=0)) 
 
# Concatenate along columns (Axis 1) - same as hstack 
print(np.concatenate((matrix_a, matrix_b), axis=1)) 