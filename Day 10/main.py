inp = [list(map(int, x.strip())) for x in open("Day 10\input.txt")]
side_length = len(inp)

#Part 1:
def inBounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < side_length and pos[1] < side_length

heads = []

for x in range(side_length):
    for y in range(side_length):
        if inp[x][y] == 0:
            heads.append((x,y))
          
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]  
  
s = 0  

for head in heads:
    stack = [head]
    endings = set()
    while stack:
        v_x, v_y = stack.pop()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]    
            if inBounds((new_x, new_y)) and inp[new_x][new_y] == inp[v_x][v_y] + 1:
                if inp[new_x][new_y] == 9:
                    if (new_x,new_y) not in endings:
                        s += 1
                        endings.add((new_x,new_y))
                else:
                    stack.append((new_x, new_y))

print(s)    

#Part 2:
s = 0  

for head in heads:
    stack = [head]
    while stack:
        v_x, v_y = stack.pop()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]    
            if inBounds((new_x, new_y)) and inp[new_x][new_y] == inp[v_x][v_y] + 1:
                if inp[new_x][new_y] == 9:
                    s += 1
                else:
                    stack.append((new_x, new_y))

print(s)