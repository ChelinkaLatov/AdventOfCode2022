lines = [line.strip() for line in open("input", "r")]
cycle, register = 0, 1
sum = 0

def addcycle():
    global cycle,register,sum
    cycle += 1
    if cycle in [20,60,100,140,180,220]:
        #print("Cycle {} has value {} so power of {}".format(cycle, register, cycle*register))
        sum += cycle*register
    if cycle-1 in [40,80,120,160,200,240]:
        print("")
    if cycle%40 in [register, register+1, register+2]:
        print("#", end="")
    else:
        print(".", end="")
    

def update(line):
    global register
    if line == "noop":
        addcycle()
    else:
        addcycle()
        addcycle()
        register += int(line.split(' ')[1])

for line in lines:
    update(line)

print("\nFinal sum is", sum)