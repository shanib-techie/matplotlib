import matplotlib.pyplot as plt
##fig, ax = plt.subplots(nrows,ncols,figsuze=(width,height))
fig , ax =plt.subplots(1,2,figsize=(10,5))
x = [1,2,3,4]
y = [10,30,45,60]
ax[0].plot(x,y,color="orange")
ax[0].set_title("line_plot")
ax[1].bar(x,y,color="red")
ax[1].set_title("bar chart")
# fig,ax = plt.subplot(2,1,shaex=True)

plt.tight_layout()
# plt.savefig("compare_graph.pdf",dpi=300,bbox_inches="tight")
# 
plt.show()