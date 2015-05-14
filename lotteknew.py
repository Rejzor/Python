import urllib2
f=urllib2.urlopen("http://www.mbnet.com.pl/dl.txt") # Wczytuje plik
list = range(1,50) # Tworze liste do przyrownania
counter={} # Tworze pusty slownik

for lines in f:
    tab_lines=lines.split(" ") #DZiele po spacji zeby miec same wylosowane liczby
    formated_tab=tab_lines[-1].strip().split(',')  # Formatuje otrzymane tab_lines by nie bylo przecinkow i \n
    for i in formated_tab:
        if int(i) in list:   #Sprwadzamn czy liczba jest w liscie jesli tak to dodaje ja do slownika i zaznaczam to dodajac +1
    			counter[i] = counter.get(i, 0) + 1
sumall=sum(counter.values())     # Sunuhe wszystkie wartosci slownika
for number, value in counter.items():  #Petla ktora wyswietla mi wszystie wylosowane numery wraz z liczba ile razy zostaly wylosowane oraz jaki to byl procent wszystkoich
	print ('Number {} drawn {} times and it is {}/10000 of all ').format(number,value,10000*value/sumall)