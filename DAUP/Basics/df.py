import pandas as pd 
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) 
df3 = pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]}) # Different column 'C' 
df_concat_diff = pd.concat([df1, df3], axis=0) 
print(df_concat_diff) 

df_outer_0 = pd.concat([df1, df3], axis=0, join='outer') 
print(df_outer_0) 

df_concat_inner = pd.concat([df1, df3], axis=0, join='inner', ignore_index=True) 
print(df_concat_inner) 

df_outer_1 = pd.concat([df1, df3], axis=1, join='outer') 
print(df_outer_1) 