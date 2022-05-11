q = [
    "stepan",
    "anna",
    "ivanova",
    "anna",
    "stepan1",
    "anna2",
    "vlad",
    "arina",
    "ivanova",
    "vlad_ivanov",
    "stepan",
    "arina",
    "stepan15",
    "ivanova",
    "arina_ivanova"
]
q_set = set()
q_list = list()

for n in q:
    q_set.add(n)
    q_list.append(n)
    if len(q_set) == len(q_list):
        print("Можно зарегестрировать пользователя: ", n)
    else:
        print("Нельзя зарегестрировать пользователя: ", n)
        q_list.pop(-1)
