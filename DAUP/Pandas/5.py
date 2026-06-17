import pandas as pd
import matplotlib.pyplot as plt
data = {
'Name': ['A', 'B', 'C', 'D'],
'Age': [25, 30, 35, 40],
'City': ['New York', 'London', 'New York', 'Paris']
}
df = pd.DataFrame(data)

# Bar Chart
plt.bar(df['Name'], df['Age'], color='skyblue')
plt.title('Age of Individuals - Bar Chart')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()
