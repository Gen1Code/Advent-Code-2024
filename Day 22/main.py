inp = [int(x.strip()) for x in open("Day 22\input.txt")]

#Part 1:

def loop(s):
    t = s << 6
    s = s ^ t
    s = s & 16777215
    
    t = s >> 5
    s = s ^ t
    s = s & 16777215
    
    t = s << 11
    s = s ^ t
    s = s & 16777215
    return s

su = 0
for x in inp:
    for i in range(2000):
        x=loop(x)
    su += x
    
print(su)

#Part 2:
sequences = {}

for x in inp:
    tracking = (0,0,0,0)
    last = 0
    inp_seq = {}
    for i in range(2000):       
        x = loop(x)
        
        p = x % 10
        n = p - last
        last = p
        
        tracking = (tracking[1], tracking[2], tracking[3], n)
        if i > 2:
            if tracking in inp_seq:
                continue
            inp_seq[tracking] = p 
    
    for sequence, price in inp_seq.items():
        sequences[sequence] = sequences.get(sequence,0) + price
    

print(max(sequences.values()))    