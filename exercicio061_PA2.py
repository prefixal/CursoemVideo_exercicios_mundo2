primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
count = 0

while count < 10:
	print('{} -> '.format(termo), end='')
	termo += razao
	count += 1
print("FIM!")
