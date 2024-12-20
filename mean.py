import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","kavya","kavya","kavya"],
                "marks":[7,5,12,9,8,21,14,16,25]})
df
a=df['marks']
b=a.mean()
print(b)