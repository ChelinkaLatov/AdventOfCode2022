line = open("input", "r").readline().strip()
N = 14
for i in range(len(line)-N):
    dico = {i:0 for i in line[i:i+N]}
    if len(dico) == N:
        print("The first instruction is at {}".format(i+14))
        exit()