# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, 
# а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

import sys
import operator


# https://drive.google.com/file/d/1TsMBziDQxiqSa1YGgOAD_XHQh-4HuY6r/view?usp=sharing

print('Простой калькулятор\n0 в качестве знака операции - выход')

try:
    while True:
        sign = input('Введите знак операции ')
            
        while sign != '+' and sign != '-' and sign != '*' and sign != '/':
            if sign == '0': 
                sys.exit()
            print('Неверный знак операции')
            sign = input('Введите знак операции ')

        num1 = int(input('Введите первое число '))
        num2 = int(input('Введите второе число '))
        
        if sign == '+': 
            res = operator.add(num1, num2)
        elif sign == '-': 
            res = operator.sub(num1, num2)
        elif sign == '*': 
            res = operator.mul(num1, num2)
        elif sign == '/':
            while num2 == 0:
                print('Деление на ноль')
                num2 = int(input('Введите второе число '))
            res = operator.truediv(num1, num2)

        print(res)
        
except SystemExit:
    pass
