"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = input('Введите натуральное число: ')


def count_evens_odds(num):
    evens = 0
    odds = 0
    for i in num:
        if int(i) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'{evens=}, {odds=}'


print(count_evens_odds(number))