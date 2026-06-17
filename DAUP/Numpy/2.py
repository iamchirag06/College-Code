import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("1D Array Dimensions:", arr1.ndim) 
print("Shape of the array:",arr1.shape)
print("Shape of the array:",arr1.size)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array Dimensions:", arr2.ndim) 
print("Shape of the array:", arr2.shape)
print("Shape of the array:", arr2.size)
print("Normal array: \n",arr2)
print("Transpose:\n",arr2.T)

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array Dimensions:", arr3.ndim)
print("Shape of the array:", arr3.shape)
print("Shape of the array:", arr3.size)
print(arr3.T)


