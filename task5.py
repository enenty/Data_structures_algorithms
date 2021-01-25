"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква
"""
import string


position = int(input('Введите номер буквы в английском алфавите: '))
letter = (ord('a') + position) - 1
print(chr(letter))


# секретный бонус-левел (2 вариант)
alphabet = string.ascii_lowercase
alphabet = alphabet[position-1:position]
print(alphabet)