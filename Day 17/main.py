inp = [x.strip() for x in open("Day 17\input.txt")]
r_a = int(inp[0][12:])
r_b = int(inp[1][12:])
r_c = int(inp[2][12:])

p = list(map(int, inp[4][9:].split(",")))
p_l = len(p)

#Part 1:
def run(a,b,c,p):
    o = []
    i_p = 0
    
    def combo(ope):
        if ope<4:
            return ope
        elif ope == 4:
            return a
        elif ope == 5:
            return b
        elif ope == 6:
            return c
        if ope == 7:
            print("Legacy")
    
    while i_p < p_l:
        jumped = False
        opc = p[i_p]
        ope = p[i_p+1]
        
        if opc == 0:
            a = int(a/(2**combo(ope)))
        elif opc == 1:
            b = b^ope
        elif opc == 2:
            b = combo(ope) % 8
        elif opc == 3:
            if a != 0:
                jumped = True
                i_p = ope
        elif opc == 4:
            b=b^c
        elif opc == 5:
            o.append(combo(ope) % 8)
        elif opc == 6:
            b = int(a/(2**combo(ope)))
        elif opc == 7:
            c = int(a/(2**combo(ope)))

        if not jumped:
            i_p += 2
    
    return o

output = run(r_a,r_b,r_c,p)
print(','.join(map(str, output)))

#Part 2:
#2,4: b = a%8
#1,1: b = b^1
#7,5: c = a/(2**b) (trunc)
#4,4: b = b^c
#1,4: b = b^4
#0,3: a = a/(2**3) (trunc)
#5,5: out b % 8             (only important part per loop)
#3,0: jump to 0 if a != 0   (for loop depends entirely on a)

def step(a):
    b = a % 8
    b = b^1
    c = int(a/(2**b))
    b = b^c
    b = b^4
    return b % 8

stack = []

#Stack things, smallest on top
for a in range(7,-1,-1):
    stack.append((p_l-1,a))

while stack:
    idx, a = stack.pop()
    
    if step(a) != p[idx]:
        continue

    if idx == 0:
        print(a)
        break
    
    for r in range(7, -1, -1): 
        stack.append((idx - 1, a*8 + r))
