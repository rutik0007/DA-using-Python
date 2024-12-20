import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {'name':['a','b','c','d','e','f','g','h'],
  'maths': [95, 90, 99, 104, 105, 94, 99, 104],
'bio': [23,45,67,89,90,45,67,89],
'age':[12,23,34,45,56,67,78,89]}
df = pd.DataFrame(data)

print(df)
df1=df.corr()
print(df1)

sns.heatmap(df1,annot=True,cmap='RdBu')
plt.show()