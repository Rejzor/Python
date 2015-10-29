from itertools import permutations
tab=input().split(" ")
tab[1]=int(tab[1])
wynik = sorted(list(permutations(tab[0],tab[1])))
for i in wynik:
	print(''.join(i))
