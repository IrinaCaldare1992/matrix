garden = [
    #   0,   1,  2 
    [ '*', 'v', 'v' ],   # 0
    [ 'v', '.', '.' ],   # 1 
    [ 'v', '.', '.' ]    # 2
]

for row in garden:
    for col in row:
        print( col, end=' ' )
print() 

roses  = 0
tulips = 0
empty_space = 0

for ri in garden:
    for ci in ri:
        if ci == "*":
            roses += 1
        elif ci == "v":
            tulips += 1
        elif ci == ".":
            empty_space += 1
print("roses: ", roses, "tulips: ", tulips, "empty spaces: ", empty_space)