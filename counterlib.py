from collections import Counter
import urllib2

f=urllib2.urlopen("http://www.mbnet.com.pl/dl.txt") 
counter = Counter()

for lines in f:
    tab_lines = lines.split()  # note, no argument!
    formatted_tab = map(int, tab_lines[-1].split(','))
    #print formatted_tab
    counter.update(i for i in formatted_tab if 0 < i < 50)

print counter.most_common()