words = ["яблоко", "кот", "программирование", "дом", "молоко"]
students = [("Аня", 20), ("Борис", 18), ("Вера", 22), ("Глеб", 19)]
nums = [33, 12, 45, 21, 8, 99]
print(sorted(words, key=len))
print(sorted(students, key=lambda std: std[1]))
print(sorted(nums, key=lambda num: str(num)[-1]))
