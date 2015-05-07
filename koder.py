import string
def koder():
	print("Wporwadz tekst do zakodowania")
	tekst=list(input(": "))
	#print(tekst)
	print("Kod Cezara o ile przesunac ? Podaj liczbe")
	przesuniecie=input(": ")
	#print(przesuniecie)
	baza=list("{}{}{}{}".format(string.ascii_letters,string.punctuation,string.digits," "))
	kod=""

	for i in tekst:
		if i in baza:
			kod += baza[(baza.index(i)+int(przesuniecie))%(len(baza))]
	print ('Twoj zakodwany kod to: {}'.format(kod))
koder()