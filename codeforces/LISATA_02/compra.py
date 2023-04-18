valor_produto = int(input())
qtd_produto = int(input())
valor_pago = int(input())
a_pagar = valor_produto * qtd_produto
troco = valor_pago - a_pagar
print("A pagar: {0}\nTroco  : {1}".format(a_pagar, troco))