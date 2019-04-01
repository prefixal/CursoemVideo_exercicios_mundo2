nt1 = float(input("Digite a primeira nota: "))
nt2 = float(input("Digite a segunda nota: "))
nt3 = float(input("Digite a terceira nota: "))

media = (nt1+nt2+nt3)/3

print("Sua média foi de {:.2f}".format(media))

if media < 5:
	
	print("Aluno REPROVADO!")

elif media >= 7:

	print("Aluno APROVADO. Parabéns!")
	
else:
	
	print("Aluno em RECUPERAÇÃO!")
	