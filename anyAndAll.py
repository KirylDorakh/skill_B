# any

print(any([2 == 2, 3 == 2]))
print(any([True, False, False]))
print(any([False, False]))

#############
dict = {False: False, True: False}

print(any(dict))

#############

old_list = [2, 1, 3, 8, 10, 11, 13]
list_if_even = list(map(lambda x: x % 2 == 0, old_list))
list_if_odd = [x % 2 != 0 for x in old_list]

print(list_if_even)
print(list_if_odd)

print("Are any of the elements even? " + str(any(list_if_even)))
print("Are any of the elements odd? " + str(any(list_if_odd)))

###########
# all

print(all([2 == 2, 3 == 2]))
print(all([2 > 1, 3 != 4]))
print(all([True, False, False]))
print(all([False, False]))

################

old_list = ["just", "Some", "text", "As", "An", "example"]
list_begins_upper = list(map(lambda x: x[0].isupper(), old_list))
list_shorter_than_8 = [len(x) < 8 for x in old_list]

print(list_begins_upper)
print(list_shorter_than_8)

print("Do all the strings begin with an uppercase letter? " + str(all(list_begins_upper)))
print("Are all the strings shorter than 8? " + str(all(list_shorter_than_8)))
