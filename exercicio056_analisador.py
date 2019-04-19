somaidade = 0
#mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0

for i in range(1,4):
	print('--'*3 + "{}ª PESSOA".format(i) + '--'*3)
	nome = input("Nome: ")
	idade = int(input("Idade: "))
	sexo = input("Sexo [M/F]: ")
	somaidade += idade
	if i == 1 and sexo in 'Mm':
		maioridadehomem = idade
		nomevelho = nome
	if sexo in 'Mm' and idade > maioridadehomem:
		maioridadehomem = idade
		nomevelho = nome
	if sexo in 'Ff' and idade < 20:
		totalmulher20 += 1
mediaidade = somaidade / 3
	
print("A média de idade do grupo é {:.2f} anos.".format(mediaidade))
print("O homem mais velho tem {:.2f} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totalmulher20))