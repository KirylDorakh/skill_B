a = []
t = None

while t != 0:
    t = int(input())
    a.append(t)
a.pop()

# удаление повторяющихся элементов
a = list(set(a))

cond = None
cond2 = None

for elem in a:
    if cond is None or elem > cond:
        cond2 = cond
        cond = elem
        print("промежуточные вычисления1: ", cond, cond2)
    elif cond2 is not None and elem > cond2:
        cond2 = elem
        print("промежуточные вычисления2: ", cond, cond2)

print(cond)
print(cond2)
