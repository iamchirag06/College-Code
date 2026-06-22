import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# Sample Data 
data = { 
'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 
'Sales': [100, 150, 200, 180, 250] 
} 
df = pd.DataFrame(data) 
# 1. Bar Chart 
plt.figure(figsize=(5,3)) 
plt.bar(df['Month'], df['Sales'])
plt.xlabel("Month")
plt.ylabel("Sales") 
plt.title("Bar Chart") 
plt.show() 

# 2. Line Chart 
plt.figure(figsize=(5,3)) 
plt.plot(df['Month'], df['Sales'], marker='o') 
plt.title("Line Chart") 
plt.show() 

# 3. Pie Chart 
plt.figure(figsize=(5,3)) 
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%') 
plt.title("Pie Chart") 
plt.legend()
plt.show() 

# 4. Histogram
plt.figure(figsize=(5,3))
plt.hist(df['Sales'], bins=5, edgecolor='black')
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Histogram of Sales")
plt.legend()
plt.show() 