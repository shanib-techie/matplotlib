import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


score = np.array([23,44,2,1,33,44,55,6,44,3,76,88,8,77,5,44,3,5,43,2,44,6,21,23,23,4,5,77,65,43,3,2,22,11,77,6,55,4,33,7,77,52,22,46])
print(score)
print("average: ",score.mean())

plt.hist(score,bins=6,color="red",edgecolor="black")
plt.xlabel("SCORE RANGE")
plt.ylabel("COUNT OF SCORE GROUP")
plt.title('nuber of score in each group',color="pink",fontsize=18)
plt.show()
