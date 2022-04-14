n = int(input('n: '))
m = int(input("m: "))
k = int(input('k: '))

if (n + m > k) and (n + k > m) and (m + k > n):
    print('YES')
    if n < k > m:
        if n ** 2 + m ** 2 == k ** 2:
            print('right')
        if n ** 2 + m ** 2 < k ** 2:
            print ('acute')
        if n ** 2 + m ** 2 > k ** 2:
            print('obtuse')
    elif k < m > n:
        if n ** 2 + k ** 2 == m ** 2:
            print('right')
        if n ** 2 + k ** 2 < m ** 2:
            print('acute')
        if n ** 2 + k ** 2 > m ** 2:
            print('obtuse')
    elif k < n > m:
        if k ** 2 + m ** 2 == n ** 2:
            print('right')
        if k ** 2 + m ** 2 < n ** 2:
            print('acute')
        if k ** 2 + m ** 2 > n ** 2:
            print('obtuse')
    else:
        print('impossible')
else:
    print('NO')

