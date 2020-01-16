#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


from random import randint


NUM1 = []
for i in range(20):
    NUM1.append(randint(-10, 10))
print(NUM1)
NUM2 = NUM1.copy()
NUM2.sort()
MAX_NEG_NUM = None
MAX_NEG_INDEX = None
for i in range(len(NUM2)):
    if NUM2[i] >= 0 and i > 0:
        MAX_NEG_NUM = NUM2[i-1]
        MAX_NEG_INDEX = i-1
        break
    else:
        MAX_NEG_NUM = None
        MAX_NEG_INDEX = None
print(NUM2)
print(f'Число {MAX_NEG_NUM} с индексом {MAX_NEG_INDEX}')