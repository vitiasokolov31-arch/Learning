students = [
    ("Аня", 5), ("Борис", 3), ("Вера", 4),
    ("Глеб", 5), ("Дина", 2), ("Егор", 4),
    ("Жанна", 5), ("Зоя", 3)
]
students = list(filter(lambda student: student[1] >= 4, students))
students.sort(key=lambda student: student[1], reverse=True)
for student in students:
    print(*student)
avg = sum(list(map(lambda student: student[1], students))) / sum(list(map(lambda student: 1, students)))
print(f"Средний балл: {avg}")
