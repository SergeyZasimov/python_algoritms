# https://drive.google.com/file/d/18s8uY9To7zxD0tQxrZrQxidqm-rrscS0/view?usp=sharing

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

N = int(input('Введите трёхзначное число '))

a = N % 10
N = N // 10

b = N % 10

c = N // 10

my_sum = a + b + c
my_mul = a * b * c

print('Сумма цифр ', my_sum, '\nПроизведение цифр', my_mul)
