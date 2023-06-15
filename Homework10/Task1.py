# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_string(n1, n2):
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(n1, n2)))


def generate_random_name():
    while True:
        yield '{} {}'.format(generate_string(1, 15), generate_string(1, 15))
# Здесь пишем код


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
