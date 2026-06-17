
try:
    a = int(input("Enter Numerator:"))
    b = int(input("Enter Denominator:"))
    result=a/b
    print("Result:",result)

finally:
    print("This block will always execute")
        
print("End of execution")