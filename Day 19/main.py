inp = [x.strip().split(", ") for x in open("Day 19\input.txt")]
patterns = inp[0]

#Part 1:
from collections import deque 

s_letter = {}
done_sections = set()

for p in patterns:
    done_sections.add(p)
    if p[0] in s_letter:
        s_letter[p[0]].append(p)
    else:
        s_letter[p[0]] = [p]
    
possible = []
for i in range(2,len(inp)):
    match = inp[i][0]
    match_l = len(match)
    queue = deque([0])
    indices_done = set()

    while queue:       
        t_l = queue.popleft()
                
        if t_l in indices_done:
            continue
        
        indices_done.add(t_l)
        
        if match[t_l:] in done_sections:
            possible.append(i)
            break
                
        ps = s_letter[match[t_l]]
        for p in ps:
            p_l = len(p)
            if p == match[t_l:t_l+p_l]:
                if p_l + t_l == match_l:
                    possible.append(i)
                    queue = []
                    break
                queue.append(t_l+p_l)
    
print(len(possible))

#Part 2:
arrangements = 0
for t in possible:
    match = inp[t][0]
    match_l = len(match)
    combinatorics = {0:1}
    for i in range(1, match_l+1):
        c = 0
        cut = match[-i:]
        
        for p in s_letter[cut[0]]:
            p_l = len(p)
            if p == cut[:p_l]:
                c += combinatorics[i-p_l]
        
        combinatorics[i] = c
    
    arrangements += combinatorics[match_l]

print(arrangements)