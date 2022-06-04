n = 9478
while True:
    if n % 2 == 0:
         n = n / 2
         print("четное", n)

    else:
        n = ((n * 3) + 1) / 2
        print("нечетное", n)

    if n == 1:
        print("result", n)
        break