# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Введите X точки A: '))
y1 = int(input('Введите Y точки A: '))
x2 = int(input('Введите X точки B: '))
y2 = int(input('Введите Y точки B: '))

# y1 = k * x1 + b
# y2 = k * x2 + b
# b = y1 - k * x1
# y2 = k * x2 + y1 - k * x1
# y2 = k * (x2 - x1) + y1
# y2 - y1 = k * (x2 - x1)

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой имеет вид: y = {k}x + {b}')
