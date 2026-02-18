import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_excel("C:\\Users\\Admin\\OneDrive\\Desktop\\power bi\\retail_store_analysis\\Retail-Store-Transactions (1).xlsx")
print("overall : ",df.describe())
print(df)
print("unique va",df["Product"].unique())
k = df["Product"]
plt.xlabel("products ")
plt.ylabel("count of eeach product")
print("count of product")
plt.hist(k,bins=4,color="pink",edgecolor="black") # iss row meyeh perticular work kitni baar aya h graph me ajata h



# print(df["Product"])
# score = np.array([23,44,2,1,33,44,55,6,44,3,76,88,8,77,5,44,3,5,43,2,44,6,21,23,23,4,5,77,65,43,3,2,22,11,77,6,55,4,33,7,77,52,22,46])
# print(score)



# print("average: ",score.mean())

# plt.hist(score,bins=6,color="red",edgecolor="black")
# plt.xlabel("SCORE RANGE")
# plt.ylabel("COUNT OF SCORE GROUP")
# plt.title('nuber of score in each group',color="pink",fontsize=18)
plt.show()