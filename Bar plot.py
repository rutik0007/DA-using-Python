import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[7,15,7]
plt.bar(x,y,color="g",align="center")
plt.bar(x2,y2,color="m",align="center")
plt.title("Information")
plt.xlabel("x axis")
plt.ylabel("y axis")
