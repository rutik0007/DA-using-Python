import numpy as np

values = np.array([1,2,3,4,5])
weights=np.array([0.1,0.2,0.3,0.2,0.2])

weighted_mean=np.average(values,weights=weights)

print("weighted mean:",weighted_mean)