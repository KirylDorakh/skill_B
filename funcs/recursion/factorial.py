def fact(num):
    print(f"num - {num}")
    if num == 1:
        return num
    return fact(num - 1) * num


result = fact(3)
print(result)