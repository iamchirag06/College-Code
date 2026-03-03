#       Function Argument

# def add(num1=1,num2=0): #default Argument
#     return num1+num2

# def add(num1,*num2): #varibale length value
#     sum=num1
#     for n in num2:
#         sum+=n
#     return sum

# result=add(4,6,5,7)

# print(result)

def person(name,**kwlargs):
    print("name:",name)
    for k,v in kwlargs.items():
        print(k,":",v)
    
person(age=30,name="Chirag",loc="Pune",tech="Python") #KeyWord Argument