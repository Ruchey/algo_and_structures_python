"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

max_n = 0
for i in range(10):
    num = input("Введите натуральное число: ")
    a = 0
    for j in num:
        a += int(j)
    if a > max_n:
        max_n = a
        max_num = num
print(f"Наибольшая сумма чисел у числа {max_num}")