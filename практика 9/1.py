import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2 * np.pi, 250)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set(xlim=(-20, 20), ylim=(-20, 15), aspect='equal')
ax.axis('off')
line, = ax.plot([], [], color='crimson', lw=2)
point, = ax.plot([], [], 'o', color='crimson')

def update(i):
    line.set_data(x[:i + 1], y[:i + 1])
    point.set_data([x[i]], [y[i]])

anim = FuncAnimation(fig, update, frames=250, interval=30, repeat=False)
plt.show()