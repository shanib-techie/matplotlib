import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variance    value mean se kitna dur h
# plt.pie(vluee,labels=label_list,color=color_list,autopct="%1.1f")

df = pd.read_excel("C:\\Users\\Admin\\OneDrive\\Desktop\\power bi\\retail_store_analysis\\Retail-Store-Transactions (1).xlsx")
print(df)

print(df["PaymentType"].value_counts())



print("lacation wise sale :",df["Location"].value_counts())
k = df["PaymentType"]
print("unique of location " ,df["Location"].unique())
pym = df["PaymentType"].value_counts()
plt.title("pie of payment ")
plt.pie(pym,labels=pym.index,autopct="%1.1f%%",colors=["red","yellow","pink","green","blue"])#label  pie ki per seace ki valy

# emplname = ["shanib","ahmed","ujju","bobby","kanay"]
# incomee =[10000,300000,34000,10000,30000]
# plt.pie(incomee,labels=emplname,autopct="%1.1f%%",colors=["pink","green","red","yellow","blue"])
# plt.title("income of employee")
plt.show()
