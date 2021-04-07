## Matplotlib template example to save time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

########################################
# Powers: Plotting points
########################################
fig, axs = plt.subplots(1, 2)
fig.set_size_inches(12, 5)

xx = np.arange(0, 5, 0.5)
yy = xx**2
zz = xx**3
ww = xx**4
uu = xx**5

ax = axs[0]
ax.plot(xx, yy, label="square", color='green', linestyle="", marker="*")
ax.plot(xx, zz, label="cube", color='orange')
ax.set_xlabel("Input to the function")
ax.set_ylabel("Function output")
ax.set_title("Some function")
ax.grid()
ax.legend()

ax = axs[1]
ax.plot(xx, ww, label="4th", color='black', linestyle="", marker="o")
ax.plot(xx, uu, label="fifth", color='purple')
ax.set_xlabel("Input to the function")
ax.set_ylabel("Function output")
ax.set_title("Some function")
ax.grid()
ax.legend()

fig.savefig("img/powers.jpg", dpi=100, bbox_inches="tight") 
# dpi=300 good for printing
plt.show()

########################################
# Iris: Plotting bar graphs
########################################

iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df = iris.groupby("species").mean()
N = len(df.columns)

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(12, 7)

ind = np.arange(N) # the x-location for the groups
width = 0.15 # bar width

ax.set_ylabel("Size")
ax.set_xticks(ind)
ax.set_xticklabels(df.columns)
ax.set_title("Average iris parameters across species")
ax.grid()

y0 = df.loc["setosa", :]
rects0 = ax.bar(ind-width, y0, width)
y1 = df.loc["versicolor", :]
rects1 = ax.bar(ind, y1, width)
y2 = df.loc["virginica", :]
rects2 = ax.bar(ind+width, y2, width)
ax.legend((rects0[0], rects1[0], rects2[0]), df.index)

fig.savefig("img/iris.jpg", dpi=100, bbox_inches="tight") 
plt.show()
