#Array
from array import *

arr1  = array('i',[33,45,24,78])

#Copying Array
arr2 = array('i',arr1.tolist())

arr1[3]=0

print(arr1)
print(arr2)

print(type(arr2))
