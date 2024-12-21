inp = [list(x.strip()) for x in open("Day 21\input.txt")]

key_to_index = {
    "0":(3,1),
    "A":(3,2),
    "1":(2,0),
    "2":(2,1),
    "3":(2,2),
    "4":(1,0),
    "5":(1,1),
    "6":(1,2),
    "7":(0,0),
    "8":(0,1),
    "9":(0,2)
}

key_d_to_index = {
    "^":(0,1),
    "A":(0,2),
    "<":(1,0),
    "v":(1,1),
    ">":(1,2)
}

#Part 1:
s = 0

p1_seqs = {}
p2_seqs = {}

di = [key_to_index, key_d_to_index]
seqs_map = [p1_seqs, p2_seqs]
gap = [(3,0),(0,0)]

for i in range(2):
    for key,pos in di[i].items():
        for key2,pos2 in di[i].items():
            my = pos2[0] - pos[0]
            mx = pos2[1] - pos[1]
            
            sy = "v^"[my<0]*abs(my)
            sx = "<>"[mx>0]*abs(mx)
            
            if mx == 0:
                if my == 0:
                    seqs_map[i][(key,key2)] = [""]
                    continue
                seqs_map[i][(key,key2)] = [sy]
                continue
            
            if my == 0:
                seqs_map[i][(key,key2)] = [sx]
                continue             
            
            seq = [sy+sx, sx+sy]
            
            if pos[0] == gap[i][0] and pos2[1] == gap[i][1]:
                seq.remove(sx + sy)
            elif pos[1] == gap[i][1] and pos2[0] == gap[i][0]:
                seq.remove(sy + sx)
            
            seqs_map[i][(key,key2)] = seq

for x in inp:
    part1_seqs = [""]
    
    prev = 'A'    
    for i in range(len(x)):
        cur = x[i]
        paths = p1_seqs[(prev,cur)]
        tmp_build = []
        for j in range(len(part1_seqs)):
            for k in range(len(paths)):
                tmp_build.append(part1_seqs[j]+paths[k]+"A")
        part1_seqs = tmp_build                            
        prev = cur

    part2_seqs = set()
    
    for seq in part1_seqs:
        part2_sub_seqs = [""]
        prev = 'A'    
        for i in range(len(seq)):
            cur = seq[i]
            paths = p2_seqs[(prev,cur)]
            tmp_build = []
            for j in range(len(part2_sub_seqs)):
                for k in range(len(paths)):
                    tmp_build.append(part2_sub_seqs[j]+paths[k]+"A")
            part2_sub_seqs = tmp_build                            
            prev = cur

        for sq in part2_sub_seqs:
            part2_seqs.add(sq)
        
    part2_seqs = list(part2_seqs)    
    part3_seqs = set()
    
    for seq in part2_seqs:
        part3_sub_seqs = [""]
        prev = 'A'    
        for i in range(len(seq)):
            cur = seq[i]
            paths = p2_seqs[(prev,cur)]
            tmp_build = []
            for j in range(len(part3_sub_seqs)):
                for k in range(len(paths)):
                    tmp_build.append(part3_sub_seqs[j]+paths[k]+"A")
            part3_sub_seqs = tmp_build                            
            prev = cur

        for sq in part3_sub_seqs:
            part3_seqs.add(sq)

    s += min(len(x) for x in part3_seqs) * int(''.join(x[:3]))

print(s)

#Part 2:
inp = [x.strip() for x in open("Day 21\input.txt")]

dp = {}

def control_r(seq, depth):
    if depth == 0:
        return len(seq)

    if (seq, depth) in dp:
        return dp[(seq, depth)]

    m = p2_seqs
    if depth == 26:
        m = p1_seqs

    total = 0
    pairs = []
    prev = "A"
    for i in range(len(seq)):
        cur = seq[i]
        pairs.append((prev,cur))
        prev = cur

    for pair in pairs:
        paths = m[pair]
        min_len = float('inf')

        for path in paths:
            min_len = min(min_len, control_r(path+"A", depth-1))

        total += min_len

    dp[(seq, depth)] = total
    
    return total

s = 0
for x in inp:   
    s += control_r(x, 25+1) * int(x[:3])

print(s)