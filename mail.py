table = [
    ("Anna", 5),
    ("Vlad", 13),
    ("Denis", 1),
    ("Stepan", 43),
    ("Vera", 33),
    ("Vlad", 13),
    ("Denis", 1),
    ("Stepan", 43),
    ("Arina", 15)
    #("Arina", (15, 12))
]

d_table = dict(table)
print(d_table)
f = []
queue = ["Stepan", "Denis", "Anna"]

for n in queue:
    print(d_table[n])
    f.append(d_table[n])
    print(f)
