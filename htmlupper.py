inp=" "
while inp != "":
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

	