a = int(input("Digite um lado do triângulo: "))
b = int(input("Digite outro lado do triângulo: "))
c = int(input("Digite o último lado do triângulo: "))

if (abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < c < (a+b)) == False:
	print("Este triângulo não EXISTE!") 

elif a == b or a == c or c == b:
	print("Este é um triângulo ISÓSCELES")

elif a == b == c:
	print("Este é um triângulo EQUILÁTERO")

elif a != b != c:
	print("Este é um triângulo ESCALENO")


