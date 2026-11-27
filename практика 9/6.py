import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 30, 300)
T = 20 + 70 * np.exp(-0.05 * t)

idx = np.where(T <= 40)[0][0]

fig, ax = plt.subplots()
ax.plot(t, T, color='brown', alpha=0.2)
line, = ax.plot([], [], color='red')
point, = ax.plot([], [], 'o', color='red')
txt = ax.text(1, 85, '')

ax.axhline(40, ls='--', color='orange')
ax.text(0.5, 41, 'Питьевая 40°C', color='orange')
ax.axhline(20, ls='--', color='blue')
ax.text(13, 22, 'Комнатная 20°C', color='blue')

ax.set(xlim=(0, 27), ylim=(15, 95), xlabel='Минуты', ylabel='Температура, °C', title='Чай остывает по закону Ньютона')
ax.grid()

def update(i):
    line.set_data(t[:i+1], T[:i+1])
    point.set_data([t[i]], [T[i]])
    txt.set_text(f't = {t[i]:.1f} мин\nT = {T[i]:.1f} °C')

anim = FuncAnimation(fig, update, frames=range(idx+1), interval=20, repeat=False)
plt.show()