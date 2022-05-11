last = 0

def e():
    n = 1
    print(n)
    while True:
        e_n = (1 + 1 / n) ** n
        n += 1
        yield e_n


for a in e(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        print(a)
        last = a # иначе - присваиваем новое значение
