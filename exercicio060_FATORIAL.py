cent = 1
fat = int(input("Digite um número inteiro: "))

print('Calculando {}! = '.format(fat), end='')
while fat > 0:
    print('{}'.format(fat), end='')
    print(' x ' if fat > 1 else ' = ', end='')
    cent *= fat 
    fat -= 1

print("{}".format(cent))