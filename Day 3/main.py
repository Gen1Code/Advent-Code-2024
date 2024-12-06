inp = "".join(open("Day 3\input.txt").readlines())

#Part 1: O(n), O(1)
length = len(inp)
sum = 0
i = 0

while i+4 < length:
    if inp[i:i+4] != "mul(":
        i += 1
        continue
        
    a = 0
    ni = -1
    
    for x in range(3,0,-1):
        if inp[i+4:i+4+x].isdigit():
            ni = i+4+x
            a = int(inp[i+4:ni])
            break
        
    if ni == -1 or ni > length or inp[ni] != ',':
        i += 4
        continue
    
    b = 0
    nii = -1
    
    for x in range(3,0,-1):
        if inp[ni+1:ni+1+x].isdigit():
            nii = ni+1+x
            b = int(inp[ni+1:nii])
            break
            
    if nii == -1 or nii > length or inp[nii] != ')':
        i += 4
        continue        
    
    sum += a*b
    i = nii + 1

print(sum)

#Part 2: O(n), O(1) (using regex iter)
import re
match_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
match_dos = r"(do(?:n't)?)\(\)|" + match_mul

do = True
sum = 0

for ma in re.finditer(match_dos, inp):
    if ma.group(1):
        if ma.group(1) == "don't":
            do = False
        else:
            do = True
    else:
        if do:
            sum += int(ma.group(2)) * int(ma.group(3))

print(sum)