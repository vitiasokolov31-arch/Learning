#GUI - (Graphical user interface) - графический интерфейс пользователя, при котором человек управляет программой

#Tkinter - стандартная библиотека python для GUI

import tkinter as tk
#Создаем главное окно
window = tk.Tk()

#Устанавлиаем загаловок
window.title("Мое первое приложение")

#Устанавливаем размер окна
window.geometry("600x400+100+100") # 100 отступ от левого края и от верхенго края

#Поменять цвет экрана
window.configure(bg="lightblue")

#Запрещает менять размер окна
#window.resizable(width=False, height=False) #ширина и высота

#Минимальный размер окна
window.minsize(300,200)

#Виджет - отдельный элемент графического интерфейса, который выполняет определенную функцию

label = tk.Label(
    window,
    text='Hello World!', #Текст
    font=("Arial", 18), # Шрифт и размер
    fg='pink', #Цвет текста
    bg='blue' #Цвет квадратика
)

label.pack()

def say_hello():
    print("hello world")

button = tk.Button(
    window,
    text="Нажми меня",
    font=("Arial", 18),
    command=say_hello
)

button.pack()

entry = tk.Entry(window)
entry.pack()

#Запускаем приложение
window.mainloop()

