km_p_litro = int(input())
distancia_aero = int(input())
gasolina_existente = int(input())

litros_necessarios = distancia_aero / km_p_litro
if litros_necessarios <= gasolina_existente:
        abastecer = 0.0
        print(abastecer)
else:
    abastecer = abs(gasolina_existente - litros_necessarios)
    print(f"{abastecer:.1f}")