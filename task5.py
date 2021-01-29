"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(5):
    array_sum = 0
    answer = input('Введите 4 элемента массива через пробел')
    new_array = answer.split(' ')
    new_array = [int(i) for i in new_array]
    for num in new_array:
        array_sum += num
    new_array.append(array_sum)
    matrix.append(new_array)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print('')

