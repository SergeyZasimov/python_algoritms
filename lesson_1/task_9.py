# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num1 = int(input('Введите целое число -  первое число '))
num2 = int(input('Введите целое число -  второе число '))
num3 = int(input('Введите целое число -  третье число '))

if num1 < num2 < num3:
    print(num2)
elif num2 < num1 < num3:
        print(num1)
else:
    print(num3)
