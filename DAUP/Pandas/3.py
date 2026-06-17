import pandas as pd
df1 = pd.DataFrame({'Name': ['A'], 'Age': [25]})
df2 = pd.DataFrame({'Name': ['B'], 'Age': [30]})
# Concatenate column-wise
df3 = pd.DataFrame({'Name': ['C'], 'City': ['Paris']})
df_mixed = pd.concat([df1, df3], ignore_index=True)
print(df_mixed)