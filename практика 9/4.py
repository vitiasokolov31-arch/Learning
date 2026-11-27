import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

S = np.linspace(8, 2, 300)
C = 12 / S

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(S, C, color='brown', alpha=0.2)
line, = ax.plot([], [], color='brown', lw=2)
point, = ax.plot([], [], 'o', markersize=10)
ax.text(0.15, 6.2, 'S → 0:\nкофе → ∞', color='red')
txt = ax.text(4.8, 6.5, '', fontsize=12)

ax.set(xlim=(0, 8.5), ylim=(0, 7),
       xlabel='Часы сна S', ylabel='Чашки кофе C(S)',
       title='Сколько кофе нужно, чтобы выжить')
ax.grid()

def update(i):
    line.set_data(S[:i+1], C[:i+1])
    point.set_data([S[i]], [C[i]])
    point.set_color('green' if S[i] >= 5 else 'orange' if S[i] >= 3 else 'red')
    txt.set_text(f'сон = {S[i]:.1f} ч   кофе = {C[i]:.1f}')

anim = FuncAnimation(fig, update, frames=len(S), interval=20, repeat=False)
plt.show()