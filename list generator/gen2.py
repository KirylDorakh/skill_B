L = [[j * i for j in range(11)] for i in range(1, 11)]

for i in range(len(L)):
    print(f"список умножения для {i+1} от 0 до 10:", L[i])