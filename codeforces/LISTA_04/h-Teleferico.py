capacidade = int(input())
quantidade_alunos = int(input())

monitor = 1

qtd_viagens = quantidade_alunos // (capacidade - monitor)
resto =  quantidade_alunos % (capacidade - monitor)
if resto > 0:
    qtd_viagens += monitor
    print(qtd_viagens)
else:
    print(qtd_viagens)
