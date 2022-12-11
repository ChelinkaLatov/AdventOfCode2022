forest = [line.strip() for line in open("input", "r").readlines()]
L = len(forest)

def check_nearby(forest, tree):
    x, y = tree[0], tree[1]
    size = int(forest[x][y])
    for l in [[int(forest[x][j]) for j in range(0,y)][::-1], [int(forest[x][j]) for j in range(y+1,L)], [int(forest[j][y]) for j in range(0,x)][::-1], [int(forest[j][y]) for j in range(x+1,L)]]:
        if size > max(l):
            return True
    return False

def get_scenic(forest, tree):
    x, y = tree[0], tree[1]
    size = int(forest[x][y])
    count = 1
    for l in [[int(forest[j][y]) for j in range(0,x)][::-1], [int(forest[x][j]) for j in range(0,y)][::-1], [int(forest[j][y][::-1]) for j in range(x+1,L)], [int(forest[x][j]) for j in range(y+1,L)]]:
        s = 0
        for j in l:
            s+=1
            if j >= size:
                break
        #print(s, l)
        count *= s
    return count

somme = 2*L + 2*(L-2)
maximum = 0
for i in range(1,L-1):
    for j in range(1,L-1):
        t = get_scenic(forest, (i, j))
        print(t, maximum)
        if t > maximum:
            maximum = t
        if check_nearby(forest, (i, j)):
            somme += 1
print("---Final Count is {}---".format(somme))
print("---Max scenic score is {}---".format(maximum))