num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1  > num2:
	print("{} é maior que {}.".format(num1, num2))

elif num2 > num1:
	print("{} é  maior que {}.".format(num2,num1))

else:
	print("Ambos os números são iguais.")