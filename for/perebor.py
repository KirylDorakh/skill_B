a = []
t = None

while t != 0:
    t = int(input())
    a.append(t)

a.pop()
n = 0
print(a)
for i in range(len(a) - 1):
    print("element i:", i)
    f = 0
    for j in range(len(a) - 1 - i):
        print("element j:", j)
        if a[j] >= a[j + 1]:
            print("---")
            a[j], a[j +1] = a[j + 1], a[j]
            print("change: ", a)
            f = 1
            print("f: ", f)
            n += 1
            print("number of change:", n)
            print("---")
        if f == 0:
            print("---")
            print("no change:", a)
            print("---")
