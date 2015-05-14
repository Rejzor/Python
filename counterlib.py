from collections import Counter
import urllib2

f=urllib2.urlopen("http://www.mbnet.com.pl/dl.txt") 
counter = Counter()

for lines in f:
    tab_lines = lines.split()  # note, no argument!
    formatted_tab = map(int, tab_lines[2].split(','))
    #print formatted_tab
    counter.update(i for i in formatted_tab if 0 < i < 50)

print counter.items()

sumall=sum(counter.values())     # Sunuhe wszystkie wartosci slownika
for number, value in counter.items():  #Petla ktora wyswietla mi wszystie wylosowane numery wraz z liczba ile razy zostaly wylosowane oraz jaki to byl procent wszystkoich
	print ('Number {} drawn {} times and it is {}/10000 of all ').format(number,value,10000*value/sumall)