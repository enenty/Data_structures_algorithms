"""
Определить, какое число в массиве встречается чаще всего.
"""
import random as rnd

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_freq = array[0]
max_count = 1


for i in array:
    count = 0
    for num in range(len(array)):
        if i == array[num]:
            count += 1
        if count > max_count:
            max_count = count
            max_freq = i

print(f'{max_freq} имеет {max_count} совпадений')

