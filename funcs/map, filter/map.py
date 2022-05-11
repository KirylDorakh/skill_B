List = list(map(int, input().split()))

print(List)

#######################################################
# можно использовать любую функцию без скобок


def x_plus_2(x):
    return x + 2


mapped_list1 = list(map(x_plus_2, List))

print(mapped_list1)

# map, filter() возвращает объект map, filter, который является итератором,
# выдающим элементы по запросу. Вот почему вам нужно вызвать list(),
# чтобы создать желаемый объект списка. ###
#########################################################

numbers = [-2, -1, 0, 1, -2]

abs_values = map(abs, numbers)
print(list(abs_values))

print(list(map(float, numbers)))

print(list(map(lambda num: num ** 2, numbers)))

####################### with str ##################################
words = ['Welcome  ', '  to...', 're  al', '...life']

print(list(map(len, words)))
print(list(map(str.capitalize, words)))
print(list(map(str.strip, words)))
print(list(map(lambda s: s.strip('.'), words)))

######### Обработка множественных итераций с помощью map, filter()
# pow() принимает два аргумента, x и y, и возвращает x в степени y

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))

print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
print(list(map(lambda x, y, z: x + y + z, [1, 2], [3, 4], [5, 6])))


