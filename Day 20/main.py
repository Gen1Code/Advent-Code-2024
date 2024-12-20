inp = [x.strip() for x in open("Day 20\input.txt")]
side_length = len(inp)

start = (0,0)
end = (0,0)
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == "S":
            start = (x,y)
        elif inp[y][x] == "E":
            end = (x,y)
        
def inBounds(pos):
    return pos[0] >=0 and pos[1] >=0 and pos[0] < side_length and pos[1] < side_length        

#Part 1:
import heapq
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

path = {}

def djstrika():
    queue = [(0, start)]
    distances = {start: 0}
    previous = {start: None}

    while queue:
        d, pos = heapq.heappop(queue)
        
        if pos == end:
            path_i = []
            while pos:
                path_i.append(pos)
                pos = previous[pos]
            return list(reversed(path_i))
        
        if d > distances.get(pos, float('inf')):
            continue
        
        for dx, dy in directions:
            next_p = (pos[0] + dx, pos[1] + dy)
            
            if inBounds(next_p) and inp[next_p[1]][next_p[0]] != "#" and d+1 < distances.get(next_p, float('inf')) :
                distances[next_p] = d + 1
                previous[next_p] = pos
                heapq.heappush(queue, (d+1, next_p))
    
    return 0

p = djstrika()

for i in range(len(p)):
    path[p[i]] = i

delta = [
    (0,2),
    (0,-2),
    (2,0),
    (-2,0),
    (1,1),
    (-1,-1),
    (-1,1),
    (1,-1)
]

cheats_100_plus = 0

for node,v in path.items():
    for i in range(8):
        nx = node[0] + delta[i][0]
        ny = node[1] + delta[i][1]
        
        if inBounds((nx,ny)) and path.get((nx,ny),0) - v -2 >= 100:
            cheats_100_plus += 1
            
print(cheats_100_plus)

#Part 2:
cheats_100_plus = 0
for node,v in path.items():
    for node2,v2 in path.items():
        deltax = abs(node[0] - node2[0])
        deltay = abs(node[1] - node2[1])
        if v2 - v - (deltax + deltay) >= 100 and deltax + deltay <= 20:            
            cheats_100_plus += 1
            
print(cheats_100_plus)