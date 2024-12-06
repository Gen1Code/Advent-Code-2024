inp = [list(map(int,x.strip().split(" "))) for x in open("Day 2\input.txt")]

#Part 1: O(n*m), O(1) 
#m = Length of Level
def isSafe(level):
    prev = level[0]
    decrease = level[0] > level[1]
    for i in range(1,len(level)):
        diff = prev-level[i]
        if abs(diff) > 3 or (decrease and diff <= 0) or (not decrease and diff >= 0):
            return False
        prev = level[i]
    return True

safe = 0
for level in inp:
    if isSafe(level):
        safe +=1
   
print(safe)

#Part 2: O(n*m), O(1)
def isDampSafe(level):
    prev = level[0]
    decrease = level[0] > level[1]
    for i in range(1,len(level)):
        diff = prev-level[i]
        if abs(diff) > 3 or (decrease and diff <= 0) or (not decrease and diff >= 0):
            return isSafe(level[0:i-1]+level[i:]) or isSafe(level[0:i]+level[i+1:]) or (i == 2 and isSafe(level[0:i-2]+level[i-1:]))
        prev = level[i]
    return True

safe = 0
for level in inp:
    if isDampSafe(level):
        safe += 1
        
print(safe)
