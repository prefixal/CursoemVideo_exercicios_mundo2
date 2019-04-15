import random 

print("Suas opções: \n")

print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

jogada = int(input("Selecione sua opção: "))

computador = random.randrange(0,3)

if jogada == computador:
	print("Empate!")

elif jogada == 0:
	if computador == 1:
		print("Computador ganhou!")
	else:
		print("Jogador ganhou!")

elif jogada == 1:
	if computador == 0:
		print("Jogador ganhou!")
	else: 
		print("Computador ganhou!")

elif jogada == 2:
	if computador == 1:
		print("Jogador ganhou!")
	else:
		print("Computador ganhou!")

print(jogada)
print(computador)
 #Pedra empata com Pedra e ganha de Tesoura
 #Tesoura empata com Tesoura e ganha de Papel
 #Papel empata com Papel e ganha de Pedra


