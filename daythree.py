rucksacks = [line.strip() for line in open("input", "r").readlines()]

def remove_doubles(chaine):
    clean=""
    for letter in chaine:
        if letter in clean:
            continue
        clean += letter
    return clean

def get_priority(l):
    if l.islower():
        return ord(l)-96
    else:
        return ord(l)-38

rucksacks_pairs = []
for rucksack in rucksacks:
    rucksacks_pairs.append([remove_doubles(rucksack[:len(rucksack)//2]), remove_doubles(rucksack[len(rucksack)//2:])])

somme = 0
for pair in rucksacks_pairs:
    for letter in pair[0]:
        if letter in pair[1]:
            somme += get_priority(letter)
            break
print(somme)

# Part 2

rucksacks_clean = [remove_doubles(r) for r in rucksacks]

somme = 0
for i in range(len(rucksacks_clean)//3):
    for letter in rucksacks_clean[3*i]:
        if letter in rucksacks_clean[3*i+1] and letter in rucksacks_clean[3*i+2]:
            somme += get_priority(letter)
            break
print(somme)