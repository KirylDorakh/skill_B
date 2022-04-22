L = [i for i in range(10)]
print(f'L = {L}')

M = [i for i in range(10, 0, -1)]
print(f'M = {M}')

N = [L[i]*M[i] for i in range(10)]
print(f'N = {N}')


# Функция zip() в Python создает итератор,
# который объединяет элементы из нескольких источников данных.

for a, b in zip(L, M):
    print('a=', a, 'b=', b)

K = [a*b for a, b in zip(L, M)]
print(K)

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
print(type(zipped_values))
zipped_list = list(zipped_values)

print(zipped_list)

employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)