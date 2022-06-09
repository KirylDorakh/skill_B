def my_func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


my_func()


def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_


print(adder(1, 2, 3, 4))


def multi(*nums):
    multi = 1
    for num in nums:
        multi *= num

    return multi


print(multi(1, 2, 3))
