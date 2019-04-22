import random

num = random.randrange(0,11)
count = 0

print("Sou seu computador...\n")
print("Acabei de pensar em um número entre 0 a 10.")
print('Será que você consegue adivinhar qual foi?')
print(num)

user = int(input('Qual é seu palpite? '))

while user != num:
    
    if user < num:
        print('Mais... Tente mais um vez.')
        user = int(input('Qual é seu palpite? '))
        count += 1
    elif user > num:
        print('Menos... Tente mais um vez.')
        user = int(input('Qual é seu palpite? '))
        count += 1
    else:
        break
    
print('Acertou! Após {} tentativas'.format(count))


