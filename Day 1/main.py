inp = [list(x.strip().split("   ")) for x in open("Day 1\input.txt")]

#Part 1: O(nlogn), O(n)
left = []
right = []
for x in inp:
    left.append(int(x[0]))
    right.append(int(x[1]))

left.sort()
right.sort()
total_dist = 0

for i in range(len(left)):
    total_dist += abs(left[i]-right[i])
    
print(total_dist)

#Part 2: O(n), O(n)
left = []
right = []
for x in inp:
    left.append(int(x[0]))
    right.append(int(x[1]))

freq = {}
for i in range(len(right)):
    freq[right[i]] = freq.get(right[i],0) + 1

sum = 0
for x in left:
    sum += x*freq.get(x,0)
print(sum)
