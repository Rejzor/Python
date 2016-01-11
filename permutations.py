from itertools import combinations
t1,t2 = input().split()
t2=int(t2)
s=sorted(t1)
print (sorted(list(combinations(t1,t2))))

