inp = [x.strip() for x in open("Day 23\input.txt")]

connections = {}

#Part 1:
for x in inp:
    p1, p2 = x.split("-")
    
    if p1 in connections:
        connections[p1].add(p2)
    else:
        connections[p1] = set([p2])
        
    if p2 in connections:
        connections[p2].add(p1)
    else:
        connections[p2] = set([p1])
        
t_triangles = set()
        
for node,e in connections.items():
    if node[0] != "t":
        continue
    
    for node2 in e:
        for node3 in connections[node2]:
            if node3 in e:
                t_triangles.add(tuple(sorted([node,node2,node3])))
                
                
print(len(t_triangles))

#Part 2:
#https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def BronKerchs(r, p, x):
    if not p and not x:
        return len(r), r
    
    max_s = 0
    max_cliq = set()
    
    p_c = set(p)
    
    for v in p_c:
        n_v = connections[v]
        size, cliq = BronKerchs(r|{v}, p&n_v, x&n_v)
        p = p - {v}
        x = x | {v}
        
        if size > max_s:
            max_s = size
            max_cliq = cliq
    
    return max_s, max_cliq

_, cliq = BronKerchs(set(),set(connections.keys()),set())
print(",".join(sorted(cliq)))
