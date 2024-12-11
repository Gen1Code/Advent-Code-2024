#Part 1:
with open("Day 11\input.txt") as file:
    inp = list(map(int, file.readline().split(" ")))

for n in range(25):
    i=0
    while i < len(inp):
        a = str(inp[i])
        d = len(a)
        if inp[i] == 0:
            inp[i] = 1
        elif d % 2 == 0:
            inp[i] = int(a[:d//2])
            inp.insert(i+1,int(a[d//2:]))
            i += 1
        else:
            inp[i] *= 2024
        i += 1
        
print(len(inp))

#Part 2:
import math
with open("Day 11\input.txt") as file:
    inp = list(map(int, file.readline().split(" ")))

rule2 = {}
rule3 = {}
stones = {}
for s in inp:
    stones[s] = stones.get(s,0) + 1

for n in range(75):
    ns = {}
    for s, num in stones.items():
        if s == 0:
            ns[1] = ns.get(1,0) + num
            continue
        
        if s in rule2:
            p1,p2 = rule2[s]
            ns[p1] = ns.get(p1,0) + num
            ns[p2] = ns.get(p2,0) + num
            continue
        
        if s in rule3:
            ns[rule3[s]] = ns.get(rule3[s],0) + num
            continue
        
        d = int(math.log10(s)) + 1

        if d % 2 == 0:
            p1,p2 = divmod(s, 10**(d//2))
            rule2[s] = [p1,p2]

            ns[p1] = ns.get(p1,0) + num
            ns[p2] = ns.get(p2,0) + num
        else:
            a = s * 2024
            rule3[s] = a
            ns[a] = ns.get(a,0) + num

    stones = ns
        
print(sum(stones.values()))