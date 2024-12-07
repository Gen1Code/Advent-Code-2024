inp = [x.strip().split(" ") for x in open("Day 7\input.txt")]
results = [int(x[0][:-1]) for x in inp]
elems = [list(map(int,x[1:])) for x in inp]

#Part 1:O(n*d*2^d), O(1)
#n = number of lines
#d = max number of elements per line
sum = 0

def calc(vals, r):
    v = vals[0]
    for i in range(1,len(vals)):
        if r & (1 << (i-1)):
            v = v + vals[i]
        else:
            v = v * vals[i]
    return v

for i in range(len(elems)):
    e = elems[i]
    for r in range(2**(len(e)-1)):
        if calc(e,r) == results[i]:
            sum += results[i]
            break
        
print(sum)

#Part 2:
sum = 0

def calc3(vals, r):
    v = vals[0]
    for i in range(1,len(vals)):
        oper = (r >> (2*(i-1))) & 3
        if oper == 0:
            v = v +vals[i]
        elif oper == 1:
            v = v * vals[i]
        else:
            v = int(str(v) + str(vals[i]))
    return v

for i in range(len(elems)):
    e = elems[i]
    for r in range(4**(len(e)-1)):
        if calc3(e,r) == results[i]:
            sum += results[i]
            break
        
print(sum)