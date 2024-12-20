import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
variable=[12,10,15,18]
plt.hist(variable,bins=10)
plt.title("Histogram")
plt.xlabel("variable")
plt.ylabel("frequency")


plt.show()
y=variable.std()