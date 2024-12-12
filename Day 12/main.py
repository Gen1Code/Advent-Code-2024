inp = [list(x.strip()) for x in open("Day 12\input.txt")]
side_length = len(inp)

#Part 1:
def inBounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < side_length and pos[1] < side_length

pos_not_checked = set([(x,y) for x in range(side_length) for y in range(side_length)])

s = 0
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]  

while pos_not_checked:
    pos = pos_not_checked.pop()
    val = inp[pos[0]][pos[1]]
    stack = [pos]
    area = 1
    perim = 0
    while stack:
        (v_x, v_y) = stack.pop()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]             
            
            if inBounds((new_x, new_y)) and inp[new_x][new_y] == val:
                if (new_x, new_y) in pos_not_checked:
                    stack.append((new_x, new_y))
                    pos_not_checked.remove((new_x, new_y))
                    area += 1
            else:
                perim += 1
    
    s += area * perim
        
print(s)

#Part 2:
pos_not_checked = set([(x,y) for x in range(side_length) for y in range(side_length)])

def inp_val(pos):
    if inBounds(pos):
        return inp[pos[0]][pos[1]]
    return ""

s = 0
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]  
corners = [
    (1, 2),
    (1, 3),
    (0, 3),
    (0, 2)
]

while pos_not_checked:
    pos = pos_not_checked.pop()
    val = inp[pos[0]][pos[1]]
    stack = [pos]
    area = 1
    # V + F - 2 = E, (F=2) thus V=E
    vertices = 0
    
    while stack:
        (v_x, v_y) = stack.pop()
        neighbours = []
            
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i] 
            
            new_val = inp_val((new_x, new_y))     
            neighbours.append(new_val)
            
            if new_val == val:
                if (new_x, new_y) in pos_not_checked:
                    stack.append((new_x, new_y))
                    pos_not_checked.remove((new_x, new_y))
                    area += 1
        
        in_corner = [
            (v_x-1, v_y-1),
            (v_x-1, v_y+1),
            (v_x+1, v_y+1),
            (v_x+1, v_y-1)
        ]
                   
        for i in range(4):
            if neighbours[corners[i][0]] != val and neighbours[corners[i][1]] != val:
                vertices += 1
            if inp_val(in_corner[i]) != val and neighbours[corners[i][0]] == val and neighbours[corners[i][1]] == val:
                vertices += 1

    s += area * vertices
        
print(s)