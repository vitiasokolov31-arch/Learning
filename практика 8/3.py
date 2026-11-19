import numpy as np
import matplotlib.pyplot as plt

names = ['Маргарита Мания', 'Пепперони-Парад', 'Гавайский Хаос', 'Четыре Сыра и Слёзы', 'Веганский Бунт']
sales = np.array([23, 45, 56, 78, 32])

x = np.arange(len(names))
winner = np.argmax(sales)
print('Победитель:', names[winner], '—', sales[winner], 'пицц')

fig, ax = plt.subplots(figsize=(11, 6))

colors = ['#9db4c0'] * len(names)  # Список из 5 одинаковых цветов
colors[winner] = '#e07a5f'         # Победителю (индекс 3) — другой цвет

ax.bar(x, sales, width=0.6, color=colors, edgecolor='#3d405b', linewidth=1.5)  # Столбики: позиции x, высоты sales

ax.set_title('Битва пиццерий: продажи за неделю')
ax.set_xlabel('Пиццерия')
ax.set_ylabel('Продано пицц, шт.')

ax.set_xticks(x)
ax.set_xticklabels(names, rotation=15)  # Подписи засечек: названия вместо чисел, наклон 15°

plt.tight_layout()
plt.savefig('графики/pizzeria.png', dpi=150)
plt.show()