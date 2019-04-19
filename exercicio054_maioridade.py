import datetime

now = datetime.datetime.now()

maior = 0
menor = 0
soma_maior = 0
soma_menor = 0

for i in range(1,3):
	ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(i)))
	idade = now.year - ano

	if idade >= 18:
		maior += 1
		soma_maior += 1
	else:
		menor += 1
		soma_menor +=1

print("Ao todo tivemos {} pessoas maiores de idade. \nE também tivemos {} pessoas menores de idade.".format(maior, menor))

