a=0
b=1
counter=0
for i in range(0,input("Podaj zakres fibo: ")):
	a=a+b
	a,b=b,a
	counter+=a
	print(a)
print("SUMA: ",counter)