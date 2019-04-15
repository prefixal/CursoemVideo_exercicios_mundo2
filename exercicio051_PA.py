print("====="*8)
print("       PA OS 10 PRIMEIROS TERMOS")
print("====="*8)

num = int(input("Digite o primeiro termo da PA: "))
raz = int(input("Digite a razão da progressão: "))

for i in range(1,11):
	num += raz
	print(num, end=' ')
print("Acabou!")
