import numpy as np
import matplotlib.pyplot as plt

dist = np.array([100, 500, 1000, 3000, 5000, 10000])
ping = np.array([1.8, 5.9, 11.5, 32.5, 53.0, 104.2])

c = 300000
n = 1.5
v = c / n

P = (2 * dist / v) * 1000  # Формула применяется сразу ко ВСЕМ элементам массива dist
print('v =', v)
print('Теоретический пинг:', P)

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(dist, ping, linestyle='None', marker='o',color='tab:red', label='Измеренный пинг')
ax.plot(dist, P, linestyle='-', color='tab:blue', label='Теоретический пинг')

ax.set_title('Задержка сигнала в оптоволокне')
ax.set_xlabel('Расстояние, км')
ax.set_ylabel('Пинг, мс')

ax.set_xticks(np.arange(0, 10001, 1000))
ax.set_yticks(np.arange(0, 111, 10))

ax.grid(alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig('графики/ping_test.png', dpi=150)
plt.show()