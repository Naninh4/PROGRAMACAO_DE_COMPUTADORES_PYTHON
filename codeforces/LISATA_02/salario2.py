nome_vendedor = input()
salario = float(input())
vendas = float(input())

comicao =  vendas * 0.15
salario_total = salario + comicao

print(nome_vendedor)
print("R$ {0:.2f}".format(salario_total))