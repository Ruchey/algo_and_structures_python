"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input("Введите натуральное число: ")
even = 0
odd = 0
for i in num:
    even += int(not int(i) % 2)
    odd += int(not not int(i) % 2)
print(f'В числе {num} чётных чисел {even}, нечётных {odd}')
