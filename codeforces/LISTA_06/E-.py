def dia_da_semana(h,d):
    dia_semana = ['Domingo','Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    if d == 7:
        return dia_semana[dia_semana.index(h)]
    
    elif d<7:
        aux = dia_semana.index(h) + d
        if aux <= (len(dia_semana) - 1):
            return dia_semana[(dia_semana.index(h) +  d)]
        else:
            a = aux % 6
            return(dia_semana[a])
    elif d > 7:
        resto = (dia_semana.index(h) + d) % 7
        return dia_semana[resto]
h = input()
d = int(input())
h.lower
h.capitalize()
h.strip
print(dia_da_semana(h,d))
