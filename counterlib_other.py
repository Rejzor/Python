#!/usr/bin/env python		
liczby = {}
counter=0
file=open('baza.txt','r')
for line in file:
	x=line.split(' ')
	#print(x[2])
	a=x[2]
	for i in a.split()[-1].split(','):
		#print(i)
		if i not in liczby:
			liczby[i]=0
		liczby[i]+=1
wszystkie_liczby=sum(liczby.values())
for liczba,ilosc in sorted(liczby.items()):
	print("{} wypadlo {} razy ({}%)".format(liczba,ilosc,100*ilosc/wszystkie_liczby))