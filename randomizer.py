# Генератор рандомных цифр

import random # Модуль для рандомных цифр

numbers = random.randint(0, 1000000000) # Переменная равна рандомным цифрам
question = input('Вы хотите получить рандомное число (1, 1000000000)?: ') # Переменная, спрашивающая, хотим ли мы получить рандомное число

if question.lower() == 'да': # Если переменная равна 'да'
    print(f'Держи: {numbers}') # Вывести на экран 'Держи: {Переменная, генерирующая рандомное число}'
else: # Исключение
    print('Пока! ;(') # Вывести на экран 'Пока! ;('

# Если что-то непонятно написано, обращайтесь в Дискорд: '! RIOTOFF#0001'