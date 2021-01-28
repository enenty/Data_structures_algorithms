"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
"""

rev_string = ''
number = input('Введите целое число: ')


def reverse(num):
    global rev_string
    if int(num) < 10:
        rev_string += str(num)
        return rev_string
    else:
        last_dig = int(num) % 10
        rev_string += str(last_dig)
        num = int(num) // 10
        return reverse(num)


print(reverse(number))
