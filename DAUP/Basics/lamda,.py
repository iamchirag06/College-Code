# Standard Function 
def square_def(x): 
    return x ** 2 
 
# Equivalent Lambda Function 
square_lambda = lambda x: x ** 2 
 
print(square_def(5))     # Output: 25 
print(square_lambda(5))  # Output: 25 

# Lambda with two arguments 
add = lambda a, b: a + b 
print(add(10, 20))  # Output: 30 
 
# Lambda with three arguments 
multiply = lambda x, y, z: x * y * z 
print(multiply(2, 3, 4))  # Output: 24 
