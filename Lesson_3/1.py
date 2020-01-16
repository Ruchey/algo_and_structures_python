# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from pprint import pprint

NUM1 = []
NUM2 = []
for i in range(2, 100):
    NUM1.append(i)
for i in range(2, 10):
    NUM2.append(i)
print(NUM1)
print(NUM2)
list_k = []
for i in NUM1:
    k = 0
    for j in NUM2:
        if i % j == 0 :
            k += 1
    list_k.append(f'{i}({k})')
pprint(list_k, width=60, compact=True)