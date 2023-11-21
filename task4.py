def normalize(numbers: list[int]):
    max_val = max(numbers)
    min_val = min(numbers)
    delta = max_val - min_val

    return list(map(lambda x: (x - min_val) / delta, numbers))


def norm(array):
    max_el = max(array)
    min_el = min(array)
    return list(map(lambda x: (x - min_el) / (max_el - min_el), array))


arr = [1, 2, 3, 5,3,10]
print(normalize(arr))
