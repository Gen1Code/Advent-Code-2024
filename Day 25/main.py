locks = []
keys = []

with open("Day 25\input.txt") as f:
    text = f.read().strip()

matrices = text.split('\n\n')
for m in matrices:
    if m[:5] == "#####":
        locks.append(m.split("\n"))
    else:
        keys.append(m.split("\n"))

#Part 1:
l_h = []
for l in locks:
    height = []
    for x in range(5):
        h = 0
        for y in range(1,7):
            if l[y][x] == "#":
                h+=1
            else:
                break
        height.append(h)
    l_h.append(tuple(height))

k_h = []
for k in keys:
    height = []
    for x in range(5):
        h = 0
        for y in range(5,-1,-1):
            if k[y][x] == "#":
                h += 1
            else:
                break
        height.append(h)
    k_h.append(tuple(height))

pairs = 0
for k in k_h:
    for l in l_h:
        for x in range(5):
            if k[x] + l[x] > 5:
                break
            if x == 4:
                pairs += 1
                
print(pairs)

#Part 2:
#null ig