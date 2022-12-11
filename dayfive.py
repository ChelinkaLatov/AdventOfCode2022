from time import sleep
lines = [line[:-1] for line in open("input", "r").readlines()]

def beginning(lines):
    array = []
    for line in lines:
        if '1' in line:
            limite = int(line.strip().split()[-1])
            print("---LIMITE IS {}---".format(limite))
            break
        array.append(line)
    nice = [[line[4*i+1] for i in range(limite)] for line in array]
    col = ["" for i in range(len(nice[0]))]
    for i in range(len(nice)):
        for j in range(len(nice[0])):
            col[j] += nice[len(nice)-i-1][j]
    col = [col.strip() for col in col]
    return col,len(array)+2

structure, size = beginning(lines)
instructions = [[int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])] for line in lines[size:]]

print(structure)
for t in instructions:
    structure[t[1]-1], tomove = structure[t[1]-1][:-t[0]], structure[t[1]-1][-t[0]:]
    structure[t[2]-1] += tomove # add [::-1] for first part ^^
    print(structure)
    print(t, tomove, tomove[::-1])
    #sleep(1)

for colonne in structure:
    print(colonne[-1], end="")
