l = [2, 3, 1, 5]

def minimum(_list):

    if len(_list) == 1:
        return _list[0]
    return _list[0] if _list[0] < minimum(_list[1:]) else minimum(_list[1:])


print(minimum(l))