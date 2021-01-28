"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры
"""

length = int(input('Введите количество элементов: '))


def sum_of_n(length):
    first = 1
    el_sum = 0
    for i in range(length):
        el_sum += first
        first = first / 2 * (-1)
        return el_sum


print(sum_of_n(length))