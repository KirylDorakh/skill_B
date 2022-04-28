events = ["Anna", "Vlad", "Denis", "-", "Stepan", "-", "Vera", "-", "-", "Arina", "-", "-"]
queue = []
while len(events):
    if events[0] == "-":
        print('---')
        events.pop(0)
        print('Выдача посылки: ', queue[0])
        queue.pop(0)
        print('Осталось в очереди: ', len(queue))
    else:
        print('---')
        queue.append(events[0])
        print("В очереди плюс 1: ", queue)
        events.pop(0)



