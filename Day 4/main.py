inp = [list(x.strip()) for x in open("Day 4\input.txt")]

#Part 1: O(n^2*m), O(1)
#n = side length, m = word size
words = 0
side_length = len(inp)

def inBounds(x,y):
    return x >=0 and y>=0 and x<side_length and y<side_length

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
word = "XMAS"

for x in range(side_length):
    for y in range(side_length):
        if inp[x][y] != word[0]:
            continue
        
        for dx,dy in zip(di, dj):
            for v in range(1,len(word)):
                nx = x+dx*v
                ny = y+dy*v
                if not inBounds(nx,ny) or inp[nx][ny] != word[v]:
                    break
                
                if v == 3:
                    words += 1
print(words)
                            
#Part 2: O(n^2*m), O(1)
#n = side length, m = word size
words = 0
side_length = len(inp)

def inBounds(x,y):
    return x >=0 and y>=0 and x<side_length and y<side_length

di = [-1,-1,1,1]
dj = [-1,1,-1,1]
word = "MAS"

for x in range(side_length):
    for y in range(side_length):
        if inp[x][y] != word[1]:
            continue
        mas_found = 0
        for dx,dy in zip(di, dj):
            for v in range(-1,2,2): #depends on word size
                nx = x+dx*v
                ny = y+dy*v
                if not inBounds(nx,ny) or inp[nx][ny] != word[v+1]:
                    break
                
                if v == 1:
                    mas_found += 1
                    
        if mas_found == 2:
            words += 1

print(words)