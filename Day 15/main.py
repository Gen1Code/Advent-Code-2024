inp = [x.strip() for x in open("Day 15\input.txt")]

walls = set()
boxes = set()
robot = (0,0)
sequence = ""

parsing_maze = True
for y,l in enumerate(inp):
    if l == "":
        parsing_maze = False
        continue
    if parsing_maze:
        for x,c in enumerate(l):
            if c == "#":
                walls.add((x,y))
            elif c == "O":
                boxes.add((x,y))
            elif c == "@":
                robot = (x,y)
    else:
        sequence += l

action_direction = {
    '^': (0,-1),
    'v': (0,1),
    '<': (-1,0),
    '>': (1,0),   
}

#Part 1:
for action in sequence:
    d = action_direction[action]
    new_pos = (robot[0]+d[0], robot[1]+d[1])
    moved_box = False
    while new_pos in boxes:
        moved_box = True
        new_pos = (new_pos[0]+d[0], new_pos[1]+d[1])
    if new_pos in walls:
        continue
    robot = (robot[0]+d[0], robot[1]+d[1])
    if moved_box:
        boxes.remove(robot)
        boxes.add(new_pos)        

s = 0
for b in boxes:
    s += 100*b[1] + b[0]
print(s)

#Part 2:
grid = []

for l in inp:
    if l == "":
        break
    row = []
    for c in l:
        if c == "#":
            row.append("#")
            row.append("#")
        elif c == "O":
            row.append("[")
            row.append("]")            
        elif c == "@":
            row.append("@")            
            row.append(".")            
        else:
            row.append(".")            
            row.append(".")            
    grid.append(row)

robot = (48,24)

for action in sequence:
    print(action)
    d = action_direction[action]
    new_pos = (robot[0]+d[0], robot[1]+d[1])

    if grid[new_pos[1]][new_pos[0]] == "#":
        continue
    if grid[new_pos[1]][new_pos[0]] == ".":
        grid[robot[1]][robot[0]] = "."
        robot = new_pos
        grid[robot[1]][robot[0]] = "@" 
  
    else:
        moving = True
        stack = []
        c_to_pos = {}
        
        if grid[new_pos[1]][new_pos[0]] == "[":
            stack.append(new_pos)
        else:
            stack.append((new_pos[0]-1,new_pos[1]))

        while stack:
            checking_pos = stack.pop()

            c_to_pos[checking_pos] = "["
            c_to_pos[(checking_pos[0]+1,checking_pos[1])] = "]"
                
            next_pos = (checking_pos[0]+d[0], checking_pos[1]+d[1])
        
            if grid[next_pos[1]][next_pos[0]] == "#" or grid[next_pos[1]][next_pos[0]+1] == "#":
                moving = False
                break
            
            if grid[next_pos[1]][next_pos[0]] in "[]" and action != ">":
                if grid[next_pos[1]][next_pos[0]] == "[":
                    stack.append(next_pos)
                    
                else:
                    stack.append((next_pos[0]-1,next_pos[1]))
                    
            if grid[next_pos[1]][next_pos[0]+1] == "[" and action != "<":
                stack.append((next_pos[0]+1, next_pos[1])) 
                

        if moving:            
            for key, val in c_to_pos.items():
                grid[key[1]][key[0]] = "."
                
            for key, val in c_to_pos.items():
                assert(grid[key[1]+d[1]][key[0]+d[0]] != "#")
                grid[key[1]+d[1]][key[0]+d[0]] = val
            
            grid[robot[1]][robot[0]] = "."
            robot = (robot[0]+d[0], robot[1]+d[1])
            grid[robot[1]][robot[0]] = "@" 
            
s=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            s += i*100 +j
print(s)