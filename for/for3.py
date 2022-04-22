N = int(input('input number:'))
p = list()
print(p)

# заводим цикл for в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):
    p.append('*')
    print(p)
print("Конец цикла")


N = int(input('input number:'))

for i in range(1, N + 1):
    print('*'* i)