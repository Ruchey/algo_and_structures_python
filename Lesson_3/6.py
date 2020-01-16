"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint


NUMS = []
for i in range(20):
    NUMS.append(randint(1, 100))
MAX_NUM_INDEX = 0
MIN_NUM_INDEX = 0
for i in range(len(NUMS)):
    if NUMS[i] > NUMS[MAX_NUM_INDEX]:
        MAX_NUM_INDEX = i
    if NUMS[i] < NUMS[MIN_NUM_INDEX]:
        MIN_NUM_INDEX = i
SREZ = NUMS[min(MAX_NUM_INDEX, MIN_NUM_INDEX)+1:max(MAX_NUM_INDEX, MIN_NUM_INDEX)]
print(NUMS)
print(NUMS[MAX_NUM_INDEX], NUMS[MIN_NUM_INDEX])
print(SREZ)
SUM_SREZ = 0
for i in SREZ:
    SUM_SREZ += i
print(SUM_SREZ)