L = [4, 3, 22, 12, 4, 3, 22, 51]

def min(N):
    if len(N) == 1:
        return N[0]
    return N[0] if N[0] < min(N[1:]) else min(N[1:])

print(min(L))