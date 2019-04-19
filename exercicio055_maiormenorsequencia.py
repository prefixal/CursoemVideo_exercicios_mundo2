conj = []
for i in range(1,6):
	peso = float(input("Peso da {}ª pessoa (em kg): ".format(i)))
	conj.append(peso)

print(conj)

print("O maior valor da sequência é {:.2f}kg".format(max(conj)))
print("O menor valor da sequência é {:.2f}kg".format(min(conj)))