"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def table_symb(start, end, rows):
    for i in range(start, end, rows):
        print("Таблица символов:")
        for j in range(rows):
            if (i+j) > end:
                break
            print(f'{i+j} - {chr(i+j)}')


table_symb(32, 127, 10)