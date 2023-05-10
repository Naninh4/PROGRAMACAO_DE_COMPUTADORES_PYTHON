from unicodedata import digit


print("------------------ CALCULADORA -------------------")
print("1 - soma  ")
print("2 - Multiplicação ")
print("3 - Divisão real")
print("4 - Divisão inteira")
print("5 - Subtração")

operacao = int(input("Qual operação deseja realizar?\n-"))
n1 =  float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 * n2
elif operacao == 3:
    resultado = n1 / n2
elif operacao == 4:
    resultado = n1 // n2
elif operacao == 5:
    resultado = n1 - n2

print(f"Resultado: {resultado} ")
