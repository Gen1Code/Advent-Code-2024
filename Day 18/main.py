inp = [tuple(map(int,x.strip().split(","))) for x in open("Day 18\input.txt")]
side_length = 71

#Part 1:
import heapq

start = (0,0)
end = (70,70)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
corrupted = set()

def inBounds(pos):
    return pos[0] >=0 and pos[1] >=0 and pos[0] < 71 and pos[1] < 71

for i in range(1024):
    corrupted.add(inp[i])

def djstrika():
    queue = [(0, start)]
    distances = {start: 0}
    previous = {start: None}

    while queue:
        d, pos = heapq.heappop(queue)
        
        if pos == end:
            path = []
            while pos:
                path.append(pos)
                pos = previous[pos]
            return len(path) - 1
        
        if d > distances.get(pos, float('inf')):
            continue
        
        for dx, dy in directions:
            next_p = (pos[0] + dx, pos[1] + dy)
            
            if inBounds(next_p) and next_p not in corrupted and d+1 < distances.get(next_p, float('inf')) :
                distances[next_p] = d + 1
                previous[next_p] = pos
                heapq.heappush(queue, (d+1, next_p))
    
    return 0

print(djstrika())

#Part 2:
for i in range(1024,len(inp)):
    corrupted.add(inp[i])
    
for i in range(len(inp)-1,-1,-1):
    corrupted.remove(inp[i])
    if djstrika() != 0:
        print(",".join(map(str, inp[i])))
        break