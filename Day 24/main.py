inp = [x.strip().split(" ") for x in open("Day 24\input.txt")]

#Part 1:
from collections import deque

inp_dict = {}

def gate(p1,g,p2):
    i_1 = inp_dict[p1]
    i_2 = inp_dict[p2]
    if g == "AND":
        return i_1 & i_2
    elif g == "XOR":
        return i_1 ^ i_2
    elif g == "OR":
        return i_1 | i_2

queue = deque([])
p_wires = False
for x in inp:
    if x == ['']:
        p_wires = True
        continue
    
    if p_wires:
        queue.append(x)
    else:
        inp_dict[x[0][:-1]] = int(x[1])

z_high = 0
while queue:
    x = queue.popleft()
    if x[0] not in inp_dict or x[2] not in inp_dict:
        queue.append(x)
        continue
    inp_dict[x[4]] = gate(x[0],x[1],x[2])
    if x[4][0] == "z" and int(x[4][1:]) > z_high:
        z_high = int(x[4][1:])
    

z_gates = ['0']*(z_high+1)
for gat,out in inp_dict.items():
    if gat[0] == "z":
        z_gates[-int(gat[1:])-1] = str(out)
print(int("".join(z_gates), 2))
    
#Part 2:
queue = deque([])
p_wires = False
for x in inp:
    if x == ['']:
        p_wires = True
        continue

    if p_wires:
        queue.append(x)

io = ["x","y","z"]
def is_io_gate(a,b,o):
    return a in io or b in io or o in io

#First Case: no c_in used diff
#General Case: c_in, x_i, y_i, -> c_out, z_i
#Last Case c_out simpler
swapped = []
for p1, g, p2, _, out in queue:
    #non XOR gates that make output except last since carry
    if g != "XOR" and out[0] == "z" and int(out[1:]) != z_high:
        swapped.append(out)
    #XOR gates that arent attached to io
    elif g == "XOR" and not is_io_gate(p1[0],p2[0],out[0]):
        swapped.append(out)
    #AND Gates not the beggining of input (x00&y00) one (no carry)
    elif g == "AND" and p1 != "x00":
        #Look for non or gates fed by output
        for p1_2, g_2, p2_2, _, out2 in queue:
            if  g_2 != "OR" and (out == p1_2 or out == p2_2):
                swapped.append(out)
                break
    #XOR gates that are attached to io
    elif g == "XOR":
        #Look for or gates fed by output
        for p1_2, g_2, p2_2, _, out2 in queue:
            if g_2 == "OR" and (out == p1_2 or out == p2_2):
                swapped.append(out)
                break
    
print(",".join(sorted(swapped)))