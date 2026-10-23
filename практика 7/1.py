def func(x):
    return x ** 2 / 10 + 1
a, b = -2, 5
l = [10, 100, 1000, 10000]
for N in l:
    S = 0
    h = (b - a) / N
    for i in range(0, N):
        x_i = a + i * h
        S += func(x_i) * h
    print(f"Для N равного: {N}, интеграл будет равен: {S:.3f}")