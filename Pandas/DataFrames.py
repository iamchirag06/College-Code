import pandas as pd

# DataFrame = A tabular data structure with rows and columns. (2-Dimensional)
#             Similar to Excel Spreadsheet

data = {"Name":["Aman","Punit","Rahul"],
        "Age":[30,35,40]
    }

df = pd.DataFrame(data)
print(df)

# Custom Index
df1 = pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])
print(df1)

# Using Location Property
print("Using Lock Property")
print(df1.loc["Employee 1"])

print(df1.iloc[1])