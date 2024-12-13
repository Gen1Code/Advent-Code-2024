inp = [x.strip() for x in open("Day 13\input.txt")]

#Part 1:
tokens = 0
for i in range(0,len(inp),4):
    b_a = inp[i][12:].split(",")
    b_b = inp[i+1][12:].split(",")
    w_p = inp[i+2][9:].split(",")

    a = (int(b_a[0]),int(b_a[1][2:]))
    b = (int(b_b[0]),int(b_b[1][2:]))
    p = (int(w_p[0]),int(w_p[1][3:]))
    
    max_a = min(p[0]//a[0]+1, p[1]//a[1]+1,100)
    max_b = min(p[0]//b[0]+1, p[1]//b[1]+1,100)
    min_tokens = 401
    for j in range(max_a):
        for k in range(max_b):
            if j*a[0] + k*b[0] == p[0] and j*a[1] + k*b[1] == p[1]:
                min_tokens = min(min_tokens, 3*j+k)
    if min_tokens != 401:
        tokens += min_tokens
        
print(tokens)

#Part 2:
import sympy as sp

tokens = 0
for i in range(0,len(inp),4):
    b_a = inp[i][12:].split(",")
    b_b = inp[i+1][12:].split(",")
    w_p = inp[i+2][9:].split(",")

    a = (int(b_a[0]),int(b_a[1][2:]))
    b = (int(b_b[0]),int(b_b[1][2:]))
    p = (int(w_p[0])+10000000000000,int(w_p[1][3:])+10000000000000)
    
    A = sp.Matrix([
        [a[0],b[0]],
        [a[1],b[1]]
    ])
    B = sp.Matrix([p[0],p[1]])
    D = A.inv() * B

    if D[0].is_integer and D[1].is_integer and (D[0]*a[0] + D[1]*b[0] - p[0]).is_zero and (D[0]*a[1] + D[1]*b[1] - p[1]).is_zero:
        tokens += 3*D[0]+D[1]
        
print(tokens)