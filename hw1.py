# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from random import sample


def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index]:
                index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]


def sort_list_declarative(numbers):
    return numbers.sort()


numbers1 = sample(range(0, 100), 10)
numbers2 = sample(range(0, 100), 10)
print(numbers1)
sort_list_imperative(numbers1)
print(numbers1)
print('*' * 50)
print(numbers2)
sort_list_declarative(numbers2)
print(numbers2)
