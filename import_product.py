from itertools import *
	
tab1=map(int,input().split(" "))
tab2=map(int,input().split(" "))
tab = ([ i for i in product(tab1, tab2)])

for i in tab:
	print (i, end=" ")

