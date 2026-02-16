import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# plt.pie(vluee,labels=label_list,color=color_list,autopct="%1.1f")

# data = pd.read_csv("")
emplname = ["shanib","ahmed","ujju","bobby","kanay"]
incomee =[10000,300000,34000,10000,30000]
plt.pie(incomee,labels=emplname,autopct="%1.1f%%",colors=["pink","green","red","yellow","blue"])
plt.title("income of employee")
plt.show()
