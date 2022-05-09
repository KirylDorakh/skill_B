# Factorial

def rec(n):
    if n == 1:
        return n
    else:
        return n * rec(n - 1)


num = 5
print(f"Factorial {num} is {rec(num)}")


# Итеративный подход
def factorial_iterativ(n):
    factorial = 1
    if num < 0:
        return f"Факториал не вычисляется для отрицательных чисел ({n})"
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"Факториал {num} это {factorial}")


factorial_iterativ(num)
