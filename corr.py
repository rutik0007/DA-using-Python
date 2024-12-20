import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
'marks': [23,45,67,89,90,45,67,89],
'age':[12,23,34,45,56,67,78,89]}
df = pd.DataFrame(data)

df
df1=df.corr()
df1