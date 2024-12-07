inp = [list(x.strip()) for x in open("Day 6\input.txt")]

#Part 1:
side_length = len(inp)
distinct_pos = {}
start = (0,0)
for x in range(side_length):
    for y in range(side_length):
        if inp[x][y] == "^":
            start = (x,y)
            break

def inBounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < side_length and pos[1] < side_length

def move(pos,dir):
    if dir == 0:
        return (pos[0]-1, pos[1])
    if dir == 1:
        return (pos[0], pos[1]+1)
    if dir == 2:
        return (pos[0]+1, pos[1])
    
    return (pos[0], pos[1]-1)

cur = start
dir = 0
while True:
    if cur in distinct_pos:
        if dir in distinct_pos[cur]:
            break
        distinct_pos[cur].add(dir)
    else:
        distinct_pos[cur] = {dir}
    
    tentative = move(cur,dir)
    
    if inBounds(tentative):
        while inp[tentative[0]][tentative[1]] == "#":
            dir = (dir + 1) % 4
            tentative = move(cur,dir)
            if not inBounds(tentative):
                break   
    else:
        break
    
    cur = tentative
   
print(len(distinct_pos))

#Part 2:
ob = 0

for key in distinct_pos.keys():
    x,y = key
    if key == start:
        continue

    inp[x][y] = "#"
    distinct_pos_c = {}
    cur = start
    dir = 0
    while True:
        if cur in distinct_pos_c:
            if dir in distinct_pos_c[cur]:
                ob += 1
                break
            distinct_pos_c[cur].add(dir)
        else:
            distinct_pos_c[cur] = {dir}
        
        tentative = move(cur,dir)
        
        if inBounds(tentative):
            while inp[tentative[0]][tentative[1]] == "#":
                dir = (dir + 1) % 4
                tentative = move(cur,dir)
                if not inBounds(tentative):
                    break   
        else:
            break
        
        cur = tentative
    
    inp[x][y] = "."

print(ob)
