"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""


from random import random

num = int(random() * 100)
for i in range(1, 11):
    print(f'Попытка {i}')
    usernum = int(input("Отгадайте число от 0 до 100: "))
    if usernum == num:
        print('Вы угадали!')
        break
    if usernum > num:
        print(f'Загаданное число меньше {usernum}')
    if usernum < num:
        print(f'Загаданное число больше {usernum}')
    if i == 10:
        print(f'Вы проиграли! Загаданное число {num}')