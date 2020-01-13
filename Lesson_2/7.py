"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def sum_n(n):
    if n < 1:
        return 0
    n = n + sum_n(n - 1)
    return n


def formula(n):
    return n * (n + 1) / 2


n = int(input("Введите число: "))
sumn = sum_n(n)
forml = formula(n)
print(f'Сумма чисел 1+2+...+n = {sumn}')
print(f'Значение формулы n(n+1)/2 = {forml}')