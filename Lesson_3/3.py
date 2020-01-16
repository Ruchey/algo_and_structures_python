#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


from random import randint


NUM1 = []
for i in range(10):
    NUM1.append(randint(1, 100))
NUM2 = NUM1.copy()
INDEX_MIN = 0
INDEX_MAX = 0
for i in range(len(NUM2)):
    if NUM2[i] < NUM2[INDEX_MIN]:
        INDEX_MIN = i
    if NUM2[i] > NUM2[INDEX_MAX]:
        INDEX_MAX = i
NUM2[INDEX_MIN], NUM2[INDEX_MAX] = NUM2[INDEX_MAX], NUM2[INDEX_MIN]

print(NUM1)
print(NUM2)