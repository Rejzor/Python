inp=raw_input()
tab = []
l = len(inp)
count = 1
i = 1
while i < l:
 	if inp[i] == inp[i - 1]:
 		count += 1
 	else:
 		tab.insert(i - 1,[inp[i - 1],count])
 		count = 1
 	i += 1
tab.insert(i - 1,[inp[i - 1],count])
print tab
