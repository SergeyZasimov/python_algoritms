# 1. Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и 
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
from functools import reduce

Company = namedtuple('Company', 'name, quarter1, quarter2, quarter3, quarter4, total')

count = int(input('Количество компаний '))

companies = []

for i in range(count):
    name = input(f'\nНазвание {i+1}-ой компании ')
    quarter1 = int(input('Первый квартал '))
    quarter2 = int(input('Второй квартал '))
    quarter3 = int(input('Третий квартал '))
    quarter4 = int(input('Четвёртый квартал '))
    total = reduce(lambda x, y: x + y, (quarter1, quarter2, quarter3, quarter4))
    companies.append(Company(name, quarter1, quarter2, quarter3, quarter4, total))
print('\n')

# for company in companies:
#     print(company)

year_total = 0
for company in companies:
    year_total += company.total
average = year_total / len(companies)

print('Средняя прибыль', round(average, 2))
print('\n')

print('Предприятия, чья прибыль выше среднего')
for company in companies:
    if company.total > average:
        print(company.name)
print('\n')

print('Предприятия, чья прибыль ниже среднего')
for company in companies:
    if company.total < average:
        print(company.name)