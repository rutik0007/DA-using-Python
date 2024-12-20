import pandas as pd

df1=pd.DataFrame({"id":[1,2,3,4,5],
                 "name":["a","b","c","d","e"],
                 "age":[12,23,11,13,14],
                 "sex":["m","f","m","m","m"]})
print(df1)

df2=pd.DataFrame({"id":[1,2,3,4,5],
                 
                 "marks":[90,95,94,97,98]})
print(df2)
merge_data=pd.merge(df1,df2,on="id")
merge_data
var=pd.concat([df1,df2],axis=0)
var
var.fillna({"name":"ram","age":23,"sex":"m","marks":45})
var