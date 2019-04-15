num = int(input("Digite um número: "))
add = 0

for i in range(1, num + 1):
	if num % i == 0:
		add += 1

if add == 2:
	print("Esse número é primo.")
else:
	print("Esse número não é primo.")




#if num // num != 1:
#	print("Esse é primo.")

#else:
#	print("Talvez seja primo.")