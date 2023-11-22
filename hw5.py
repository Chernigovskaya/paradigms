# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве


from bisect import bisect_left


def binary(array, number):
    index = bisect_left(array, number)
    if index != len(array) and array[index] == number:
        return index
    return -1


arr = [1, 2, 3, 4, 5]
print(binary(arr, 50))
print(binary(arr, 3))


def binary2(arr, number):
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1
    while arr[mid] != number and low <= high:
        if number > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return -1
    else:
        return mid


print(binary2(arr, 3))
print(binary2(arr, 30))
