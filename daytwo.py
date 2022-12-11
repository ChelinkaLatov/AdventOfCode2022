with open("input", "r") as f:
    l = [line.strip() for line in f.readlines()]

def score(A, B):
    return base[A] + cond[B]

def game(A,B):
    if A == B: #Draw
        return score(B, 'D')
    elif (A == "rock" and B == "paper") or (A == "paper" and B == "scissors") or (A == "scissors" and B == "rock"):
        return score(B, 'W')
    elif (A == "scissors" and B == "paper") or (A == "rock" and B == "scissors") or (A == "paper" and B == "rock"):
        return score(B, 'L')

def getplay(A, C):
    if C == "D": # Draw case
        return base[A]
    elif C == "W": # Win case
        return base[A]% 3+1
    elif C == "L": # Lose case
        t = (base[A]-1)%3
        if t == 0:
            t = 3
        return t

cond = {"L":0,"D":3,"W":6}
tocond = {"X":"L","Y":"D","Z":"W"}
base = {"rock":1, "paper":2, "scissors":3}
you = {"A":"rock","B":"paper","C":"scissors"}
me = {"X":"rock","Y":"paper","Z":"scissors"}
somme = 0

for line in l:
    A, B = line.split(' ')
    A, B = you[A], me[B]
    somme += game(A, B)
print(somme)

somme = 0
for line in l:
    A,B=line.split(' ')
    A,B = you[A], tocond[B]
    somme += cond[B]+getplay(A, B)
print(somme)
