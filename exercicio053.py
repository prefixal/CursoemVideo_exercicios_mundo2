str = input("Digite uma frase: ")
print(str)

def reverse_slicing(s):
    return s[::-1]
    
if reverse_slicing(str) == str:
    print("A frase é um palíndromo")
else:
    print("Não é!")

print(str[1:10:2])

#parangaricutirrimirruaro