## o que é um número ímpar?

# i == impar se i % 2 != 0

## o que é divisivel por 3

## i == div por 3 se i % 3 == 0

## apenas se atender a essas duas condições ele irá somar

count = 0
soma = 0
for i in range(1,500,2):
	if i % 3 == 0:
		soma = soma + i
		count += 1
print("A soma de todos os {} valores solicitados é igual a {}.".format(valores, count))
