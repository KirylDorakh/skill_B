def get_mul_func(m):
    nonlocal_m = m
    def local_func(n):
        return n * nonlocal_m
    return local_func


result = get_mul_func(4)(2)

print(result)
