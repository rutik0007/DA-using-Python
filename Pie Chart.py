import matplotlib.pyplot as plt
players=("rohit","virat","shikhar","yuvraj")
runs=(45,30,15,10)
explode=(0.1,0,0,0)
colors=("m","g","b","y")
fig1,ax1=plt.subplots()
ax1.pie(runs,explode=explode,labels=players,colors=colors,autopct='%1.1f%%',
        shadow=True,startangle=90)
plt.legend()
plt.title("pie chart")
plt.show()