heads = 35
legs = 94

for r in range(heads + 1):
    for ph in range(heads + 1):
        if (r + ph) > heads or \
        (r * 4 + ph * 2) > legs:
            print(r, ph)
            continue
        if (r + ph) == heads and (r*4 + ph * 2) == legs:
            print('value of rabbits', r)
            print("value of phazans", ph)
            print("---")
