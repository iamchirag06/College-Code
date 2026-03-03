# map, reduce & Filter
from functools import reduce
nums =  [4,1,3,2,5,8,7,9,0,2,4,6,7,5,4,3,2,1]

evens=[]
# for i in nums:
#     if i % 2 ==0:
#         evens.append(i)

# def double_it(n):
#     return n *2

# def sum_it(a,b):
#     return a+b 

evens = list(filter(lambda n : n%2==0,nums)) #Filter

doubles = list(map(lambda n : n*2,evens)) # Map

sum = reduce(lambda a,b : a+b,doubles) #Reduce

print(evens)
print(doubles)
print(sum)