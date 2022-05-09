def calc_sum_numbers(n):
    if not n:
        return 0
    else:
        summ = calc_sum_numbers(n[1:])
        summ = summ + n[0]
        return summ


def calc_neg_numbers(n):
    if not n:
        return 0
    else:
        count1 = calc_neg_numbers(n[1:])
        if n[0] < 0:
            count1 = count1 + 1
        return count1


num = [1, 2, 3, 4, -5, -1]
print(calc_sum_numbers(num))
print(calc_neg_numbers(num))

