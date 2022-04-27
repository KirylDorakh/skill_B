def print_these(a=None, b=3, c=None):
    print(f'{a} is stored in a')
    print(f'{b} is stored in b')
    print(f'{c} is stored in c')


print_these(c=1, a=2)

###
d = [1, 2, 3]
e = [*d, 4, 5, 6]

print(e)

### *args


def print_scores(student, *scores):
    print(f"Student Name: {student}")
    for score in scores:
        print(score)


print_scores('Ivan', 1, 2, 3, 4, 5, 6)

### **kwargs


def print_pet_name(owner, **pets):
    print(f'Owner name: {owner}')
    for pet, name in pets.items():
        print(f"{pet}: {name}")


print_pet_name('Julia', dog='Reks', cat=["larry", "Barry", "Garry"], turtle='Sheldon')
