# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random

MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 11

array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(array)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

print(merge_sort(array))
