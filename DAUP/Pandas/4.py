import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'New York', 'Paris']
}

# Create DataFrame first
df = pd.DataFrame(data)

# Plot graph
df.plot(
    x='Name',
    y='Age',
    kind='line',
    title='Age by Name',
    marker='o'
)

plt.show()