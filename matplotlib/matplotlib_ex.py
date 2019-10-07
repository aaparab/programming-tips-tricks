## Matplotlib example to save time

import matplotlib.pyplot as plt
import numpy as np

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

fig.savefig("powers.png", dpi=300, bbox_inches="tight")
plt.show()