preco = float(input("Qual é o valor da compra (R$): "))
print("=== Qual a condição de pagamento? === \n")
print("[1] Dinheiro à Vista")
print("[2] 1x Cartão")
print("[3] 2x no Cartão")
print("[4] 3x ou mais no Cartão \n")
print(5*"_=_=_")

condicao = int(input("Selecione uma opção: "))

if condicao == 1:
	final = preco * 0.9
elif condicao == 2:
	final = preco * 0.95
elif condicao == 3:
	final = preco
elif condicao == 4:
	final = preco * 1.2


print("O valor final a ser pago será de R$ {:.2f}".format(final))
