num = 1
list_ = []

# все кроме 0, false, None, [] - дает true
while num:
    num = int(input('Input integer: '))
    list_.append(num)

result = sum(list_)
print(result)
