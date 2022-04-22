person = {}
person = {'name':'Ivan Petrov'}
person['name2'] = 'Ivan Petrov'
person['age'] = 25
person['email'] = 'ivan_petrov@gmail.com'
person['id', 42] = '8(800)555-35-35'
print(person)

print(person['age'])
print(person.keys())
print(person.values())
person.pop('name2')
print(person)

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))