import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6, 6))

x = [0]
y = [0]

line, = ax.plot([], [], color='blue')
point, = ax.plot([], [], 'o', color='red', markersize=8)

ax.set_title('Случайное блуждание')
ax.grid(False)

def update(i):
    dx = np.random.uniform(-1, 1)
    dy = np.random.uniform(-1, 1)
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
    line.set_data(x, y)
    point.set_data([x[-1]], [y[-1]])
    margin = 2
    ax.set_xlim(min(x) - margin, max(x) + margin)
    ax.set_ylim(min(y) - margin, max(y) + margin)

    ax.set_aspect('equal')

anim = FuncAnimation(fig, update, frames=200, interval=100, repeat=False)

plt.show()