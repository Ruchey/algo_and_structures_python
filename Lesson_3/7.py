"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""


from random import randint


NUM1 = []
for i in range(20):
    NUM1.append(randint(1, 100))
NUM2 = NUM1.copy()
NUM2.sort()
MIN1 = NUM2[0]
MIN2 = NUM2[1]
print(NUM2)
print(MIN1, MIN2)