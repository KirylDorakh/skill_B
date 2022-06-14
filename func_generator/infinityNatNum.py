def inf_nat_num(num=1, count=1):
    while True:
        num += count
        yield num



for result in inf_nat_num(100, 100):
    print(result)
