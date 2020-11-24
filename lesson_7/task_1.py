# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, 
# которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, 
# что у вас должна остаться сортировка пузырьком. 
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10

# array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]   # повторяющиеся элементы
print(array)

def upgrade_bubble_sort(arr):
    count = 0 # количесиво проходов по массиву
    while True:
        change = 0  # счётчик перестановок за один проход
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change += 1
        count += 1
        # print(arr, change)
        if change == 0: 
            break
    return(arr, count)

result1 = upgrade_bubble_sort(array)
print(result1[0])
# print(result1)

# def bubble_sort(array):
#     count = 0
#     while count < len(array):
#         for i in range(len(array) - 1):
#             if array[i] < array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#         count += 1
#         # print(array)
#     return(array, count)

# result2 = bubble_sort(array)
# print(result2)
