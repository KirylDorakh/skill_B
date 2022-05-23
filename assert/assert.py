
def avg(ranks):
    assert len(ranks) != 0, 'List is empty'
    return round(sum(ranks)/len(ranks), 2)


ranks = []
print("среднее значение: ", avg(ranks))
