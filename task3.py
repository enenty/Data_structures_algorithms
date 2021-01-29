"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random as rnd

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
maximum = 0
max_pos = 0
minimum = MAX_ITEM
min_pos = 0

for i in range(SIZE-1):
    if array[i+1] > array[i] and array[i+1] > maximum:
        maximum = array[i + 1]
        max_pos = i + 1
    if array[i] < array[i + 1] and array[i] <= minimum:
        minimum = array[i]
        min_pos = i

array[max_pos], array[min_pos] = array[min_pos], array[max_pos]
print(array)







