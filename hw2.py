# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.


def table_multiplication(num):
    for i in range(1, (num + 1)):
        print(f'1 * {i} = {i}')


number = int(input('Input number: '))
table_multiplication(number)
# процедурная