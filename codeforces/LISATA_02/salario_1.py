nome_vendedor = input()
horas_trabalhadas = int(input())
valor_hora = float(input())

salario =  horas_trabalhadas * valor_hora

print(nome_vendedor)
print("R$ {0:.2f}".format(salario))