"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

for number in range(2, 10):
    count = 0
    for i in range(2, 100):
        if i % number == 0:
            count += 1
    print(f'{number} - {count}')
