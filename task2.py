"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

print('Введите координаты двух разных точек: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 != x2 and y1 != y2:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - ((y1 - y2) / (x1 - x2)) * x2
    print(f'y = {k} * x + {b} ')
elif y1 == y2:
    print(f'y = {y1}')
else:
    print(f'x = {x1}')

