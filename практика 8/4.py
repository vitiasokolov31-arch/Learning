import matplotlib.pyplot as plt

labels = ['Спасает мир', 'Сон', 'Кибер-квесты', 'Другое']
hours = [8, 7, 5, 4]

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(hours,  # Круговая: данные, подписи секторов, проценты на секторах
       labels=labels,
       autopct='%1.1f%%',
       colors=['#e63946', '#457b9d', '#2a9d8f', '#f4a261'],  # Свои цвета секторов, по порядку
       explode=[0.01, 0.01, 0.01, 0.01],)  # Насколько выдвинуть каждый сектор из центр

ax.set_title('День супергероя Алексея')

plt.savefig('графики/superhero.png', dpi=150)
plt.show()
plt.show()