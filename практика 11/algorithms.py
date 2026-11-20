def reverse_number(n):
    """Возвращает целое число с цифрами в обратном порядке."""
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

def gcd(a,b):
    """Возвращает наибольший общий делитель чисел a и b."""
    if b == 0:
        return b
    while b != 0:
        temp = b
        b = a % b
        a =  temp
    return a

def is_prime(n):
    """Функция определяет является ли число простым"""
    if n <= 1:
        return False
    else:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            else:
                d += 1
    return True

def fibonacci(n):
    """Функция вычисляет n-e число Фибоначчи"""
    if n == 0:
        return 0
    else:
        prev, curr, i = 0, 1, 1
        while i < n:
            nxt = prev + curr
            prev, curr = curr, nxt
            i += 1
    return curr

def max_increasing_len(arr):
    """Функция принимает в себя список чисел
    и находит максимальную длину непрерывного возрастающего подотрезка"""
    if len(arr) == 0:
        return 0
    else:
        cur, best, i = 1, 1, 1
        while i < len(arr):
            if arr[i] > arr[i - 1]:
                cur += 1
            else:
                cur = 1
            best = max(cur, best)
            i += 1
        return best

def sqrt_newton(n, eps=1e-6):
    """функция приближённо вычисляет квадратный корень из неотрицательного числа n с заданной точностью eps"""
    if n == 0:
        return 0.0
    else:
        x = n / 2
        while abs(x * x - n) > eps:
            x = 0.5 * (x + n / x)
        return x

def second_max(arr):
    """функция принимает список чисел arr и возвращает второй по величине элемент среди различных значений списка."""
    inf = float("inf")
    if len(arr) < 2:
        return None
    else:
        m1, m2, i, = -inf, -inf, 0
        while i < len(arr):
            if arr[i] > m1:
                m2, m1 = m1, arr[i]
            else:
                if m2 < arr[i] < m1:
                    m2 = arr[i]
            i += 1
        return m2

def count_primes_up_to(n):
    """функция подсчитывает, сколько простых чисел содержится в диапазоне от 2 до целого числа n включительно."""
    cnt, num = 0, 2
    for num in range(2, n):
        is_p, d = True, 2
        while d ** 2 <= num and is_p:
            if num % d == 0:
                is_p = False
            d += 1
        if is_p:
            cnt += 1
    return cnt




