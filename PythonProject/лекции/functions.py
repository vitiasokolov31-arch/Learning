#Docstring = Documentation string

def greet(name):
    """Приветствует пользователя по имени"""
    print(f"Hello {name}")


greet("Виктор") #Вызов функции

help(greet) #help() - показывает Docstring
print(greet.__doc__)
help(print)

#pass - пустая операция

def ex():
    return 1, 2, 3, 4, 5

#b, e = ex() - Ошибка
b, *e = ex()
print(f"print(b, e) - {b}, {e}")


#Scope - Участок программного кода, в пределах которого переменная или имя доступно для использования
#Правило LEGB: L - local, G - global, E - enclosing, B - built-in

y = 100
def func():
    global y
    y = 300
    print(y)
func()
print(y)

#map() - применяет переданную функцию к каждому элементу
a, b = map(int, input().split())
print(a, b, sep="\n")

# lambda arg: arg ** 2 - Анонимная функция, записывающиеся в одну строку
numbers =[1,2,3,4,5]
print(tuple(map(lambda num: num + 10, numbers)))

nums = [-1,-2,0,-3,4]
print(sorted(nums, key=abs))