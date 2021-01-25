"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
import string

print('Введите две буквы алфавита от a до z')
alphabet = string.ascii_lowercase
letter_one = input('Первая: ')
letter_two = input('Вторая: ')
pos_one = alphabet.find(letter_one) + 1
pos_two = alphabet.find(letter_two) + 1
print(f'Буква {letter_one} стоит на {pos_one} месте, буква {letter_two} стоит на {pos_two} месте')
print(f'Между ними {abs(pos_two - pos_one)} букв(ы)')










