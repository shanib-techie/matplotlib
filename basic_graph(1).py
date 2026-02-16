import matplotlib.pyplot as plt

x = ["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
y = [10420,20000,3300,100000,5400,21050,10000]
# plt.plot(x,y)#show version
plt.plot(x,y,color="red",linestyle="--",linewidth=4,marker="o",label="25 sale")
plt.title("weeklysales",fontsize=12)
plt.legend(loc ="upper right",fontsize =12)
plt.xlabel("days")
plt.ylabel("income")
plt.grid(color="gray",linestyle=":",linewidth="1")
plt.xticks(["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"],["mon","tues","wed","thurs","fri","sat","sun"])
plt.show()