num = 12344321

print(str(num) == str(num)[::-1])


month = int(input('Number of month: '))

if month in [1, 2, 12]:
    print('winter')
elif month in [3, 4, 5]:
    print('spring')
elif month in [6, 7, 8]:
    print('summer')
elif month in [9, 10, 11]:
    print('autumn')
else:
    print('incorrect')

result = num if num > month else month
print(result)

