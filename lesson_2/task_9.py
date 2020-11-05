# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

print('Hайти число наибольшее по сумме цифр')

def num_sum(num):
    num_sum = 0
    while num:
        num_sum += (num % 10)
        num //= 10
    return num_sum

num_string = input('Введите через пробел последовательность чисел ')
num_string = num_string.split()
max_sum = 0

for num in num_string:
    num = int(num)
    tmp = num_sum(num)
    if tmp > max_sum:
        max_num = num
        res_sum = tmp
          
print(f'{max_num=}, {res_sum=}')
