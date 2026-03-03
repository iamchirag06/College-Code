#Global and Local Variable

a = 10 #Global Variable
def something():
    a=11 #Local Variable
    print("inside:",a)

    
something()  #Function  called
print("outside",a)