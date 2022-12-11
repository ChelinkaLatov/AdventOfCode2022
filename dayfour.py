pairs = [int(a) for line in open("input", "r") for d in line.strip().split(',') for a in d.split('-')]
sommecomprised, sommeoverlapped = 0, 0

def is_comprised(q): # tells if [a,b] is strictly inside of [c,d] (or the opposite)
    return q[0] <= q[2] and q[1] >= q[3] or q[2] <= q[0] and q[3] >= q[1]

def is_overlapped(q):
    return not(q[0] > q[3] or q[1] < q[2])

for i in range(len(pairs)//4):
    #print(pairs[4*i:4*i+4], is_comprised(pairs[4*i:4*i+4]))
    if is_comprised(pairs[4*i:4*i+4]):
        sommecomprised += 1
        sommeoverlapped += 1
        continue
    #print(pairs[4*i:4*i+4], is_overlapped(pairs[4*i:4*i+4]))
    if is_overlapped(pairs[4*i:4*i+4]):
        sommeoverlapped += 1
print("{} pairs are overlapping, {} of them have one completely inside the other.".format(sommeoverlapped, sommecomprised))