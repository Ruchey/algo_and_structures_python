"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


import cProfile


def gen(n):
    num = []
    for i in range(1, n):
        num.append(i)
    return num


def definit_prime(n):
    """Проверяет, является ли число простым"""
    if n <= 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def find_prime(arr):
    """Находим простые числа"""
    res = []
    for i in arr:
        if definit_prime(i):
            res.append(i)
    return res


def resheto(num):
    m = 2
    cnt = len(num)
    while m < cnt:
        if num[m] != 0:
            j = m * 2
            while j < cnt:
                num[j] = 0
                j = j + m
        m += 1
    res = []
    for i in num:
        if i != 0:
            res.append(i)
    return res


NUM = gen(10000)
# print(NUM)
# print(find_prime(NUM))
# print(resheto(NUM))

print('Мой метод')
cProfile.run('find_prime(NUM)')
print('Решето Эротосфена')
cProfile.run('resheto(NUM)')

# Вывод: решето работает быстрее при большем количестве массива.
# Но почему-то сам алгоритм работает не правильно, пропускает числа кратные 2
