positions = set()
N = 9 # Change to 1 for first exercise

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def dist(p,q):
    return ((p[0]-q[0])**2+(p[1]-q[1])**2)**(1/2)

def moveposX(pH, pX):
    if pH == pX: # it did not move
        return pX
    distance = dist(pH,pX)
    #print("Distance from {} to {} is {}".format(pH,pX,distance))
    if distance <= 2**(1/2):
        return pX
    if distance == 2:
        if pH[0] == pX[0]:
            return [pX[0], pX[1]-sign(pX[1]-pH[1])]
        if pH[1] == pX[1]:
            return [pX[0]-sign(pX[0]-pH[0]), pX[1]]
        print("Straight Error {} {}".format(pH, pX))
    else:
        if pH[0] > pX[0] and pH[1] > pX[1]:
            return [pX[0]+1,pX[1]+1]
        if pH[0] > pX[0] and pH[1] < pX[1]:
            return [pX[0]+1,pX[1]-1]
        if pH[0] < pX[0] and pH[1] > pX[1]:
            return [pX[0]-1,pX[1]+1]
        if pH[0] < pX[0] and pH[1] < pX[1]:
            return [pX[0]-1,pX[1]-1]
    

def move(command, posX):
    way,number = command.split(' ')
    #print(way,number)
    if way == "U":
        for i in range(int(number)):
            posX[0][0] += 1
            for i in range(0,N):
                posX[i+1] = moveposX(posX[i], posX[i+1])
            positions.add(str(posX[-1]))
    elif way == "D":
        for i in range(int(number)):
            posX[0][0] -= 1
            for i in range(0,N):
                posX[i+1] = moveposX(posX[i], posX[i+1])
            positions.add(str(posX[-1]))
    elif way == "L":
        for i in range(int(number)):
            posX[0][1] -= 1
            for i in range(0,N):
                posX[i+1] = moveposX(posX[i], posX[i+1])
            positions.add(str(posX[-1]))
    elif way == "R":
        for i in range(int(number)):
            posX[0][1] += 1
            for i in range(0,N):
                posX[i+1] = moveposX(posX[i], posX[i+1])
            positions.add(str(posX[-1]))
    #print("Head in {} Tail in {}".format(posX[0],posX[i]))
    return (posX)

lines = [line.strip() for line in open("input").readlines()]
posX = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for line in lines:
    posX = move(line,posX)
print("Total number of tiles ran over {}".format(len(positions)))
