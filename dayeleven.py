lines = [line.strip() for line in open('input', 'r')]
monkeys = {}
pgcd = 1

def monkeyturn(monkey):
    for old in monkey[0]: #its items
        monkey[-1] += 1
        new = eval(monkey[1]) % pgcd # add //3 for part 1
        if new % monkey[2]:
            monkeys[monkey[3][1]][0].append(new)
        else:
            monkeys[monkey[3][0]][0].append(new)
    monkey[0] = []

def readmonkey(pack):
    global monkeys
    #Number of the Monkey
    monkey_number = int(pack[0].split(' ')[1][:-1])
    #List of items
    ditems = pack[1].split(' ')[2:]
    items = [int(ditems[i][:-1]) if (i < len(ditems)-1) else int(ditems[i]) for i in range(len(ditems))]
    #Calcul sent in string to be eval'd
    Formula = pack[2].split("=")[1][1:]
    #Divisor
    divisor = int(pack[3].split(' ')[-1])
    #SendToWho ?
    SendTrue,SendFalse = int(pack[-2].split(' ')[-1]),int(pack[-1].split(' ')[-1])
    monkeys[monkey_number] = [items, Formula, divisor, [SendTrue, SendFalse], 0]

for i in range(len(lines)//7+1):
    readmonkey(lines[7*i:7*i+6])
print(monkeys)
div = [t[2] for t in monkeys.values()]
for d in div:
    pgcd *= d
print("PGCD", pgcd)
for i in range(10000):
    for j in range(len(monkeys)):
        monkeyturn(monkeys[j])
    print(i/100)
bus = [monkeys[monkey][-1] for monkey in monkeys]
bus.sort()
print(bus)
print("Total monkey business equals {}".format(bus[-1]*bus[-2]))