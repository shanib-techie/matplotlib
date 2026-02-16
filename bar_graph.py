import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

product = ["a","b","c","d","e"]
sales = [1000,234,4500,1000,2000]
# plt.bar(product,sales,color="orange",label="sale 25")
plt.barh(product,sales,color="orange",label="sale 25")



plt.xlabel("product")
plt.ylabel("sales")

plt.title("sale comprare")
plt.legend()
plt.show()
print("average :",np.mean(sales))