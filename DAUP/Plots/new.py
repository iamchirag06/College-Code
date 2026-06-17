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
plt.show()

# 4. Histogram
plt.figure(figsize=(5,3))
plt.hist(df['Sales'], bins=5)
plt.title("Histogram")
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(5,3))
plt.scatter(df['Month'], df['Sales'])
plt.title("Scatter Plot")
plt.show()

# 6. Box Plot
plt.figure(figsize=(5,3))
plt.boxplot(df['Sales'])
plt.title("Box Plot")
plt.show()

# 7. Heat Map
corr_data = np.array([[1, 0.8, 0.5],
                      [0.8, 1, 0.6],
                      [0.5, 0.6, 1]])

plt.figure(figsize=(4,3))
plt.imshow(corr_data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Heat Map")
plt.show()

# 8. Area Chart
plt.figure(figsize=(5,3))
plt.fill_between(df['Month'], df['Sales'])
plt.title("Area Chart")
plt.show()
