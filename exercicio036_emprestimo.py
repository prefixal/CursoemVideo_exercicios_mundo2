
casa = float(input("Digite o valor da casa em R$: "))
salario = float(input("Qual o seu salário em R$?: "))
ano = int(input("Em quantos anos irá pagar?: "))

print("Sua prestação será de R${:.2f} ao mês.".format(casa/(12*ano)))

if (casa/(12*ano)) > (0.3*(salario)):
	print("Empréstimo NEGADO!")
else:
	print("Empréstimo CONCEDIDO!")