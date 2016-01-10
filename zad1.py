# answer=[]
# for i in range(2000,3200):
# 	if(i%7==0) and (i%5!=0):
# 		answer.append(i)

# print(answer)

# tmp=1
# factorial = int(input("Podaj silnie do obliczenia: "))
# if factorial!=0:
# 	for i in range(0,factorial-1):
# 		tmp=tmp*(factorial-i)
# else:
# 	tmp=1
# print(tmp)

key=[]
val=[]
N=int(input("How many?: "))
for i in range(1,N+1):
	key.append(i)
	val.append(i*i)


print(dict(zip(key,val)))
