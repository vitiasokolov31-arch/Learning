import numpy as np  # Подключает numpy (массивы и вычисления) под коротким именем np
import matplotlib.pyplot as plt  # Подключает модуль для рисования графиков под именем plt

days = np.arange(1, 15)  # Массив дней от 1 до 14 (15 не включается)

day_t = np.array([5.1, 6.3, 4.8, 7.2, 9.5, 8.1, 6.7, 5.9, 7.4, 8.8, 10.2, 9.1, 7.5, 6.2])  # Дневная температура
night_t = np.array([-1.2, 0.3, -2.1, 1.5, 3.8, 2.4, 0.9, -0.4, 1.8, 3.2, 4.6, 2.9, 1.1, -0.3])  # Ночная температура

fig, ax = plt.subplots(figsize=(11, 6))  # Создаёт холст (fig) и оси (ax) размером 11×6 дюймов
ax.plot(days, day_t, color='tab:orange', linestyle='-', marker='o', label='Днём')  # Дневной график: оранжевая сплошная линия с кружками
ax.plot(days, night_t, color='tab:blue', linestyle='--', marker='s', label='Ночью')  # Ночной график: синяя штриховая линия с квадратами

day_mean = day_t.mean()  # Среднее значение дневной температуры
night_mean = night_t.mean()  # Среднее значение ночной температуры
ax.axhline(day_mean, color='tab:orange', linestyle=':', label='Среднее днём')  # Горизонтальная линия среднего днём (точечная)
ax.axhline(night_mean, color='tab:blue', linestyle=':', label='Среднее ночью')  # Горизонтальная линия среднего ночью (точечная)

frost_nights = np.sum(night_t < 0)  # Считает ночи с температурой ниже нуля (True = 1, False = 0)
print('Ночей с отрицательной температурой:', frost_nights)  # Выводит результат в консоль

ax.axhline(0, color='black', label='Граница мороза')  # Чёрная горизонтальная линия на уровне 0 °C

ax.set_title('Температура воздуха: день и ночь')  # Заголовок графика
ax.set_xlabel('День')  # Подпись оси X
ax.set_ylabel('Температура, °C')  # Подпись оси Y

ax.set_xticks(days)  # Засечки на оси X для каждого дня от 1 до 14

ax.grid(True, alpha=0.3)  # Включает полупрозрачную сетку

ax.legend(loc='upper left')  # Легенда из всех label в левом верхнем углу

plt.tight_layout()  # Подгоняет отступы, чтобы подписи не обрезались
plt.savefig('графики/weather.png')  # Сохраняет график в файл weather.png (обязательно до show)
plt.show()  # Отображает график в окне