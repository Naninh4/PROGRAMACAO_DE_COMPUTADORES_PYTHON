codigo, quantidade = map(int, input().split())

if codigo == 1:
    resultado = quantidade * 4.00
elif codigo == 2:
    resultado = quantidade * 4.50
elif codigo == 3: 
    resultado = quantidade * 5.00
elif codigo == 4:   
    resultado = quantidade * 2.00
elif codigo == 5:
    resultado = quantidade * 1.50

print(f"Total: R$ {resultado:.2f}")