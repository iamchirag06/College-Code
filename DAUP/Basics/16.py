# Inner Function 
def  outer():
    print("In outer function")
    
    def inner():
        print("In inner function")
        
    inner()
        
outer()
