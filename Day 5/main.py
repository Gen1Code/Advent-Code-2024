with open("Day 5\input.txt") as f:
    inp = f.read().strip().split("\n\n")

rules = inp[0].split("\n")
updates = inp[1].split("\n")

#Part 1: O(n*d*a), O(d+r*f)
#n = number of update lines
#d = longest length of an update line
#a = however intersection is affected by rules
#r = unique pages in rules
#f = max number of rules for a key
rules_pages = {}

for x in rules:
    i,j = x.split("|")
    
    if i in rules_pages:
        rules_pages[i].add(j)
    else:
        rules_pages[i] = set(j)

middle_num_sum = 0

for update in updates:
    update = update.split(",")
    ordered = True
    seen = set()
    
    for p in update:
        seen.add(p)
        if seen.intersection(rules_pages.get(p, set())):
            ordered = False
            break
                
    if ordered:
        middle_num_sum += int(update[len(update)//2])
        
print(middle_num_sum)

#Part 2: O(n*dlog(d)), O(d+r*f)
from functools import cmp_to_key

middle_num_sum = 0

def sort_update(update):
    compare = cmp_to_key(lambda l,r: -1*(l+'|'+r in rules))
    return [v for v in sorted(update, key=compare)]

for update in updates:
    update = update.split(",")
    ordered = True
    seen = set()
    
    for p in update:
        seen.add(p)
        if seen.intersection(rules_pages.get(p, set())):
            ordered = False
            break
                
    if not ordered:
        update = sort_update(update)
        middle_num_sum += int(update[len(update)//2])
        
print(middle_num_sum)