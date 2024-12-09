with open("Day 9\input.txt") as f:
    inp = [int(c) for c in f.read().rstrip()]

#Part 1:
su = 0
l = 0
r = len(inp)-1
lid = 0
rid = r/2
mem_index = 0
remaining_right = inp[r]
while l<r: 
    su += lid * (inp[l]*(2*mem_index+inp[l]-1)/2)
    mem_index += inp[l]
    space = inp[l+1]
    
    while space > 0:
        if remaining_right == 0:
            rid -= 1
            r -= 2
            remaining_right = inp[r]
            if r == l :
                break
        
        used = min(remaining_right, space)
        su += rid * (used*(2*mem_index+used-1)/2)     
        remaining_right -= used
        space -= used
        mem_index += used
   
        
    lid += 1
    l+=2

print(su)

#Part 2:
files = {}
space = {}
mem = 0
i = 0

while i < len(inp) - 2:
    files[mem] = (i//2, inp[i])
    space[mem+inp[i]] = inp[i+1]
    mem += inp[i] + inp[i+1]
    i += 2

files[mem] = (i//2, inp[i])

files_list = list(files.items())

for (mem,(fid,f_size)) in reversed(files_list):
    for s in sorted(space):
        if s+f_size > mem:
            break
        s_size = space[s]
        if s_size >= f_size:
            files[s] = (fid, f_size)
            del space[s]
            del files[mem]
            s_size -= f_size
            if s_size > 0:
                space[s+f_size] = s_size
            break
            

print(sum(fid*(f_size*(2*mem+f_size-1)/2) for (mem,(fid,f_size)) in files.items()))