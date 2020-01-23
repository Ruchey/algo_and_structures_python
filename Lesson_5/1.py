"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


COUNT = int(input('Количество предприятий: '))
ENTERPRISE = {}
AVERAGE_PROFIT_EN = {}

while COUNT:
    name = input('Название предприятия: ')
    profits = list(map(int, input('Поквартальная прибыль '
                   'I II III IV (через пробел): ').split()))
    ENTERPRISE[name] = profits
    AVERAGE_PROFIT_EN[name] = sum(profits)
    COUNT -= 1

EN_MAX_PROFIT = max(AVERAGE_PROFIT_EN.items(), key=lambda x: x[1])[0]
EN_MIN_PROFIT = min(AVERAGE_PROFIT_EN.items(), key=lambda x: x[1])[0]

print(f'Список предприятий: {ENTERPRISE}')
print(f'Средняя годовая прибыль по предприятиям: {AVERAGE_PROFIT_EN}')
print('')
print(f'Максимальная средняя прибыль у предприятия '
      f'{EN_MAX_PROFIT} = {AVERAGE_PROFIT_EN[EN_MAX_PROFIT]}')
print(f'Минимальная средняя прибыль у предприятия '
      f'{EN_MIN_PROFIT} = {AVERAGE_PROFIT_EN[EN_MIN_PROFIT]}')
