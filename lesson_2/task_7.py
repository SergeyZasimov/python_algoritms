# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел 
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

print('Доказать равенство 1+2+...+n = n(n+1)/2')

n = int(input('Введите n '))

def left_func(n):
    if n == 1:
        return 1
    return (n + left_func(n-1))

def right_func(n):
    return (n * (n + 1)) / 2

print(left_func(n) == right_func(n))
