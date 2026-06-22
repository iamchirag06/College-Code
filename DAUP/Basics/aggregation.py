import pandas as pd 
 
data = { 
    "Department": ["IT", "HR", "IT", "HR", "Sales"], 
    "Salary": [50000, 40000, 60000, 45000, 55000] 
} 
 
df = pd.DataFrame(data) 
 
print(df.groupby("Department").sum()) 
print(df.groupby("Department").agg(["sum", "mean", "max"])) 
