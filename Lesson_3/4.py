# 4.	Определить, какое число в массиве встречается чаще всего.


from random import randint


NUM1 = []
for i in range(20):
    NUM1.append(randint(1, 20))
NUM2 = NUM1.copy()
NUM2.sort()
CNT = 0
NUM = NUM2[0]
MAX_CNT = 0
NUM_MAX_CNT = 0
for i in NUM2:
    if NUM == i:
        CNT += 1
    else:
        CNT = 1
    if CNT > MAX_CNT:
        MAX_CNT = CNT
        NUM_MAX_CNT = i
    NUM = i

print(NUM1)
print(NUM2)
print(NUM_MAX_CNT, MAX_CNT)