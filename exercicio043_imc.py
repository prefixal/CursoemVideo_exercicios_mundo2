peso = float(input("Qual o seu peso (kg): "))
altura = float(input("Qual a sua altura (m): "))

imc = peso / (altura)**2

print("Seu IMC é de: {:.2f}. E você esta: ".format(imc))

if imc < 18.5:
	print("ABAIXO DO PESO.")
elif imc < 25:
	print("COM PESO IDEAL.")
elif imc < 30:
	print("COM SOBREPESO.")
elif imc < 40:
	print("OBESO.")
else:
	print("COM OBESIDADE MÓRBIDA.")