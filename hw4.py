# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


def pearson_correlation(arr1, arr2):
    delta_x = sum(arr1) / len(arr1)
    delta_y = sum(arr2) / len(arr2)
    xi_delta_x = list(map(lambda x: x - delta_x, arr1))
    yi_delta_y = list(map(lambda y: y - delta_y, arr2))

    numerator = sum(map(lambda x, y: x * y, xi_delta_x, yi_delta_y))
    denominator = (sum(map(lambda x, y: x ** 2 * y ** 2, xi_delta_x, yi_delta_y))) ** 0.5
    result = (numerator / denominator)
    return result


array1 = [1, 2, 30]
array2 = [6, 7, 8]


correlation = pearson_correlation(array1, array2)
print(correlation)

