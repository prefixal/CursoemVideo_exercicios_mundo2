numero = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para conversão: ")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")

opcao = int(input("Digite a sua opção: "))

if opcao  == 1:
	#Bloco da escolha BINÁRIO:
	bino = bin(numero)
	#print(bino[2:])
	print("{} em BINÁRIO é {}".format(numero,bino[2:]))
elif opcao == 2:
	#Bloco da escolha OCTAL:
	oito = oct(numero)
	print("{} em OCTAL é {}".format(numero,oito[2:]))
elif opcao == 3:
	#Bloco da escolha HEXADECIMAL:
	hexa = hex(numero)
	print("{} em HEXADECIMAL é {}".format(numero,hexa[2:]))

else: 
	print("Opção errada!")

#Não esquecer de fatiar as strings pq as duas primeiras casas (0 e 1) são indicadores