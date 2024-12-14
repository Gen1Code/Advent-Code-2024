inp = [x.strip().split(" ") for x in open("Day 14\input.txt")]

width = 101
height = 103

quads = [0,0,0,0]

#Part 1:
for i in inp:
    p = i[0][2:].split(",")
    v = i[1][2:].split(",")
    p_x, p_y = int(p[0]),int(p[1])
    v_x, v_y = int(v[0]),int(v[1])
    
    f_x = (p_x + 100*v_x) % width
    f_y = (p_y + 100*v_y) % height
    
    left = f_x < width // 2
    right = f_x > width // 2
    top = f_y < height // 2
    bottom = f_y > height // 2
    if left:
        if top:
            quads[0] += 1
        elif bottom:
            quads[2] += 1
    elif right:
        if top:
            quads[1] += 1
        elif bottom:
            quads[3] += 1
    
print(quads[0]*quads[1]*quads[2]*quads[3])

#Part 2:
i_p = []
i_v = []
for i in inp:
        p = i[0][2:].split(",")
        v = i[1][2:].split(",")
        i_p.append((int(p[0]),int(p[1])))     
        i_v.append((int(v[0]),int(v[1])))     
    
robots = len(i_p)

for t in range(10000):
    f_pos = set()
    pr = False
    for l in range(robots):
        f_x = (i_p[l][0] + t*i_v[l][0]) % width
        f_y = (i_p[l][1] + t*i_v[l][1]) % height
        
        f_pos.add((f_x,f_y))
    
    for y in range(height):
        in_a_row = 0
        for x in range(width):
            if (x, y) in f_pos:
                in_a_row += 1
                if in_a_row > 10 :
                    pr = True
                    break
            else:
                in_a_row = 0      
    
    if pr:
        print(t)
        for y in range(height):
            row = ""
            for x in range(width):
                row += '#' if (x, y) in f_pos else '.'
            print(row)