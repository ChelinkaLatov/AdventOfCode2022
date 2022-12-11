with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()] # Cleans the lines before working with them

elves,somme = [],0 # Creates a list of elves
for line in lines:
    if line == "": # if there is no value, then we have a full elf. We add its weight to the list and reset the somme
        elves.append(somme)
        somme = 0
    else: # continue to add to the somme
        somme += int(line)
elves.append(somme) # The last somme is not empty, we empty it here.
somme = 0
elves.sort()
print("The heaviest elf is of weight {}\nThe threemost heavy elves weight all {}".format(elves[-1], sum(elves[-3:])))