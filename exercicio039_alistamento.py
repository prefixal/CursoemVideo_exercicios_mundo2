import datetime 

now = datetime.datetime.now()

ano = int(input("Insira seu ano de nascimento: "))

delta = now.year - ano

if delta < 18:
	print("Falta(m) {} anos para você se alistar.".format(18 - delta))
elif delta > 18:
	print("Você precisará pagar multa, pois já passaram {} ano(s).".format(delta - 18))
else:
	print("Você precisa se alistar IMEDIATAMENTE!")

print(delta)

