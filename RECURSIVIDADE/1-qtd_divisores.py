def qtd_divisores(n, divisor=1):
    if divisor > n:
        return 0

    if n % divisor == 0:
        return 1 + qtd_divisores(n, divisor + 1)
    else:
        return qtd_divisores(n, divisor + 1)

print(qtd_divisores(8))
