inp = [list(x.strip()) for x in open("Day 16\input.txt")]

start = (len(inp[0])-2,1)
dir = 1

dir_to_delta = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1),
}

#Part 1:
from collections import deque 

queue = deque([(start[0],start[1],dir,0)])
min_finished = 9999999999999
locs = {}
while queue:
    pos_y, pos_x, d, p = queue.popleft()
    
    if p > min_finished:
        continue
    
    if (pos_y, pos_x, d) in locs and locs[(pos_y, pos_x, d)] < p:
        continue

    locs[(pos_y, pos_x, d)] = p
    
    
    for i in range(-1,2):
        n_p = p
        n_d = (d+i)%4
        n_delta = dir_to_delta[n_d]
        n_pos_y = pos_y+n_delta[0]
        n_pos_x = pos_x+n_delta[1]
        
        if inp[n_pos_y][n_pos_x] != "#":
            if i != 0:
                n_p += 1000
            n_p += 1
            
            if inp[n_pos_y][n_pos_x] == "E":
                if n_p < min_finished:
                    min_finished = n_p
            else:
                queue.append((n_pos_y, n_pos_x, n_d, n_p))
                
print(min_finished)

#Part 2:
queue = deque([(start[0],start[1],dir,0,[(start[0],start[1])])])
locs = {}
tiles = set()

while queue:
    pos_y, pos_x, d, p, history = queue.popleft()
    
    if p > min_finished:
        continue
    
    if (pos_y, pos_x, d) in locs and locs[(pos_y, pos_x, d)] < p:
        continue

    locs[(pos_y, pos_x, d)] = p
    
    for i in range(-1,2):
        n_p = p
        n_d = (d+i)%4
        n_delta = dir_to_delta[n_d]
        n_pos_y = pos_y+n_delta[0]
        n_pos_x = pos_x+n_delta[1]
        
        if inp[n_pos_y][n_pos_x] != "#":
            if i != 0:
                n_p += 1000
            n_p += 1
            
            n_history = history.copy()
            if (n_pos_y, n_pos_x) not in tiles:
                n_history.append((n_pos_y, n_pos_x))
            
            if inp[n_pos_y][n_pos_x] == "E":
                for t in n_history:
                    tiles.add(t)
            else:
                queue.append((n_pos_y, n_pos_x, n_d, n_p, n_history))

print(len(tiles))