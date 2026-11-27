import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 20, 400)

R = -2 * x**2 + 40 * x
peak_idx = int(np.argmax(R))
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, R, color='red', alpha=0.2)
line, = ax.plot([], [], color='red', lw=2)
point, = ax.plot([], [], 'o', color='red')

txt = ax.text(1, 200, '', fontsize=12)
ax.set_xlim(0, 20)
ax.set_ylim(0, 220)
ax.set_xlabel('Цена')
ax.set_ylabel('Выручка')
ax.set_title('Максимальная выручка')
ax.grid()

def update(i):
    line.set_data(x[:i + 1], R[:i + 1])
    point.set_data([x[i]], [R[i]])
    txt.set_text(f'Цена: {x[i]:.1f} Выручка: {R[i]:.1f}')

anim = FuncAnimation(
    fig,
    update,
    frames=range(peak_idx + 1),
    interval=20,
    repeat=False
)

plt.show()