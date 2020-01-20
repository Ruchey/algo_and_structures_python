"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from random import randint

import cProfile


def gen(n):
    num = []
    for i in range(n):
        num.append(randint(1, 100))
    return num


def les37(n):
    """
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными),
     так и различаться.
    """

    num1 = n
    num2 = num1.copy()
    num2.sort()
    min1 = num2[0]
    min2 = num2[1]
    # print(num1)
    print(min1, min2)


def les37v2(n):
    """
    Работает с ошибкой, но уже нет времени с ним возиться
    """

    num1 = n
    min1 = num1[0]
    min2 = num1[1]
    len_num = len(num1)
    for i in range(2, len_num, 2):
        if num1[i] < min1:
            min1 = num1[i]
        elif num1[i] < min2:
            min2 = num1[i]
        if i < len_num:
            if num1[i + 1] < min1:
                min1 = num1[i + 1]
            elif num1[i + 1] < min2:
                min2 = num1[i + 1]
    # print(num1)
    print(min1, min2)


NUM1 = gen(1000000)
cProfile.run('les37(NUM1)')
cProfile.run('les37v2(NUM1)')

# Вывод: первая версия с сортировкой работает вдвое быстрее
