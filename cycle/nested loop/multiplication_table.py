import antigravity

print('   ', end='')
for i in range(1, 10):
    print(f'|  {i} ', end='|')
print()
for i in range(1, 10):
    print(f'|{i}|', end='')
    for j in range(1, 10):
        if j * i < 10:
            print(f'|  {j * i} ', end='|')
        else:
            print(f'| {j * i} ', end='|')
    print()