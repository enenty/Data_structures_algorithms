"""
блок-схемы
https://drive.google.com/file/d/1dxArKQgTER7Q_nsTy0Q5gSPZ5g5yWLN4/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
x = int(input('Введиде трехзначное число от 100 до 999: '))
a = x // 100
b = x // 10 % 10
c = x % 10
sum = a + b + c
mult = a * b * c
print(f'{sum=}')
print(f'{mult=}')
