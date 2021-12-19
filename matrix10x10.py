## vacuum robot

map = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 1, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
]

### DRAW THE MAP ###

for ri in range(len(map)):
    for ci in range(len(map)):
        if map[ri][ci] == 8:
            print("#", end=" ")
        elif map[ri][ci] == 0:
            print(".", end=" ")
        elif map[ri][ci] == 1:
            print("R", end=" ")
    print()

### DRAW THE MAP ###