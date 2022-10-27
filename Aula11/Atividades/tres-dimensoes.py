lista = [
    [8,92,57],
    [71,3,0],
    [9,73,58]
]

for l in range(len(lista)):
    for c in range(len(lista[1])):
        if l == c:
            print(lista[l][c])