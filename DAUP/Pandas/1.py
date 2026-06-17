import pandas as pd

data={
    'Name':['A','B','C'],
    'Age':[25,12,34]
}

df = pd.DataFrame(data)

print(df)

data1=[
    ['Apple',1],['Banana',2]
]
df1 = pd.DataFrame(data1)
print(df1)

data_concat = pd.concat([df,df1],axis=1,join='inner')
print(data_concat)