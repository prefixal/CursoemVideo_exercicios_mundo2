import datetime

now = datetime.datetime.now()

ano = int(input("Digite o ano de seu nascimento: "))

delta = now.year - ano

print("O atleta tem {} anos.".format(delta))
print("Ele está na categoria: ")

if delta <=  9:
	print("MIRIM")
elif delta <= 14:
	print("INFANTIL")
elif delta <= 19:
	print("JUNIOR")
elif delta <= 25:
	print("SENIOR")
else:
	print("MASTER")




