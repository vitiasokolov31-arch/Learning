import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 15)
screen = np.array([4.5, 5.2, 5.8, 4.9, 6.1, 6.8, 7.2, 7.5, 8.1, 7.8, 8.5, 9.0, 9.3, 9.7])
battery = np.array([58, 52, 48, 55, 42, 38, 33, 29, 22, 25, 18, 14, 11, 8])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # Холст с двумя панелями рядом: ax1 — левая, ax2 — правая

ax1.plot(days, screen, label='Экранное время', color='green', marker='o')
ax1.set_ylim(0, 11)  # Пределы оси Y: от 0 до 11
ax1.axhline(screen.mean(), linestyle='--', label='Среднее экранное время', color='gray')
ax1.set_title('Экранное время')
ax1.set_xlabel('День')
ax1.set_ylabel('Часы')
ax1.legend(loc='upper left')
ax1.set_xticks(days)
ax2.plot(days, battery, label='Заряд', color='red', marker='o')
ax2.set_ylim(0, 100)
ax2.axhline(battery.mean(), linestyle='--',  label='Средний заряд батареи', color='gray')
ax2.set_title('Заряд батареи')
ax2.set_xlabel('День')
ax2.set_ylabel('Заряд, %')
ax2.legend(loc='upper left')
ax2.set_xticks(days)

plt.savefig('phone.png')
plt.tight_layout()
plt.show()