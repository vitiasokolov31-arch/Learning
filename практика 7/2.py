def func(x):
    return x ** 2 / 10 + 1
a, b = -2, 5
l = [10, 100, 1000]
for N in l:
    h = (b - a) / N
    S = 0
    for i in range(N + 1):
        x_i = a + i * h
        if i == 0 or i == N:
            S += func(x_i) * h / 2
        else:
            S += func(x_i) * h
    print(f"Для N равного: {N}, интеграл будет равен: {S:.3f}")
