professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]

for profession, person_list in zip(professions, persons):
    print(f'{profession}')
    for person in person_list:
        print(person)
    print()