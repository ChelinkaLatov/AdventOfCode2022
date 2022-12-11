lines = [line.strip().split(' ') for line in open("input2", "r").readlines()]

def is_command(line):
    return line[0] == "$"

def move(index, m):
    if m == "..":
        return "/".join(index.split("/")[:-1])
    elif m == "/":
        return "/"
    else:
        return index+"/"+m

def simple(d):
    p = {}
    for k in d:
        b,s = [],0
        for f in d[k]:
            if f[0] == "dir":
                b.append(f[1])
            else:
                s += int(f[0])
        b.append(s)
        p[k] = b
    return p

def get_size(d, k):
    if len(d[k]) == 1:
        return d[k][0]
    return sum([get_size(d, k+"/"+path) for path in d[k][:-1]]+[d[k][-1]])
            

dico = {}

index = ""
i = 0
while i < len(lines):
    line = lines[i]
    if line[1] == "cd":
        index = move(index, line[2])
        #print(index)
        if index not in dico.keys():
            dico[index] = []
        i+=1
    else:
        i+=1
        while i < len(lines) and not is_command(lines[i]):
            dico[index].append(lines[i])
            i+=1
dico = simple(dico)
#for k in dico:
#    print(k, dico[k])

print(dico)
dico_clean = {}
for key in dico.keys():
    dico_clean[key] = get_size(dico, key)
print(dico_clean)

print("The total sum is {}".format(sum([val for val in dico_clean.values() if val <= 100000])))

# PART 2

remove = 30000000-(70000000-dico_clean["/"])
print("There is {} units of space left, we need to empty {} units".format(70000000-dico_clean["/"], remove))
if remove <= 0:
    print("There is already enough space !")
    exit()
m = min([val for val in dico_clean.values() if val >= remove])
print("You can delete the directory that is of size {}".format(m))
print("Delete the directory '{}'".format([key[1:] for key in dico_clean if dico_clean[key] == min([val for val in dico_clean.values() if val >= remove])][0]))
