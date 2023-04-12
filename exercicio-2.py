print("Exercício 2: para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.")
numero = int(input("Digite um número: "))
resultado = []
def contar_ate_n(numero):
    for x in range (1,(numero+1)):
        resultado.append(f"{x}")

    lista = " " .join(resultado)    
    print(f"Resultado: {lista}")
contar_ate_n(numero)