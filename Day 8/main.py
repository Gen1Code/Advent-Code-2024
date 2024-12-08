inp = [list(x.strip()) for x in open("Day 8\input.txt")]
side_length = len(inp)

#Part 1: O(n^2 + f*d^2), O(n^2) (space worst case is grid filled with dif frequencies)
#n = sidelength
#f = number of frequncies (restricted by n and d)
#d = max number of elems per frequency
def inBounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < side_length and pos[1] < side_length

freq = {}
for x in range(side_length):
    for y in range(side_length):
        if inp[x][y] != '.':
            if inp[x][y] in freq:
                freq[inp[x][y]].append((x,y))
            else:
                freq[inp[x][y]] = [(x,y)]

an_loc = set()
for vals in freq.values():
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            dx = vals[i][0]-vals[j][0]
            dy = vals[i][1]-vals[j][1]
            
            n1 = (vals[i][0] + dx, vals[i][1] + dy)
            n2 = (vals[j][0] - dx, vals[j][1] - dy)
            
            if inBounds(n1):
                an_loc.add(n1)
            if inBounds(n2):
                an_loc.add(n2)
            
print(len(an_loc))

#Part 2: O(n^2 +f*d^2*n), O(n^2)
an_loc = set()
for vals in freq.values():
    for i in range(len(vals)):
        
        an_loc.add(vals[i])
        
        for j in range(i+1,len(vals)):
            dx = vals[i][0]-vals[j][0]
            dy = vals[i][1]-vals[j][1]
            
            np = (vals[i][0] + dx, vals[i][1] + dy)
            nn = (vals[j][0] - dx, vals[j][1] - dy)
            
            while inBounds(np):
                an_loc.add(np)
                np = (np[0] + dx, np[1] + dy)
            
            while inBounds(nn):
                an_loc.add(nn)
                nn = (nn[0] - dx, nn[1] - dy)
print(len(an_loc))
