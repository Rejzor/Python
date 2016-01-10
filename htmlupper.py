#Python3 html UPPER 
inp=" "
while inp != "":
	tab=[]
	inp = input("Give me input ")
	upper_area = False
	out_str = ""
	for char in inp:
		if char == '>':
			upper_area = False
		elif char == '<':
			upper_area = True
		elif upper_area:
			char = char.upper()
		out_str += char 
	print(out_str)
print(tab)


# inp=" "
# while inp != "":
# 	inp = input("Give me input ")
# 	upper_area = False
# 	tab=[]
# 	counter=0
# 	for char in inp:
# 		if char==str(i):
# 			if i >= 1:
# 			if tab[i]==tab[i+1]
# 					tab.append([])
# 					tab[i].append(i)
# 					tab[i].append(counter)

# 	print(tab)
