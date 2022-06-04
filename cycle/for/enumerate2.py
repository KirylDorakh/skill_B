print(list(enumerate('1,2,3,4,5')))

for i, el in enumerate('1,2,3,4,5'):
    print(i, el)

company_name = 'SkillFactory'
for i, letter in enumerate(company_name):
    print(f'Position of symbol "{letter}" - {i + 1}')


data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]

sum_ = 0

for i, el in enumerate(data):
    print(i, el, el[i])
    sum_ += el[i]

print(sum_)
# List compression
result = sum([el[i] for i, el in enumerate(data)])
print(result)
