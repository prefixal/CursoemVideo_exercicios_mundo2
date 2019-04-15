par = 0
imp = 0
count = 0

for i in range (1,7):
	num = int(input("Digite o valor {}: ".format(i)))
	if num % 2 == 0:
		par +=num
		count += 1
	#else:
		#imp += num

print("A soma dos {} número(s) pares é igual a {}.".format(count,par))
