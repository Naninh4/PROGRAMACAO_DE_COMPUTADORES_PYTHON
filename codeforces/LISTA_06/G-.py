def dia(dia, mes, ano):
    meses={
        1: "janeiro", #31
        2: "fevereiro",#28
        3: "março",#31
        4: "abril",#30
        5: "maio",#31
        6: "junho",#30
        7: "julho",#31
        8: "agosto",#31
        9: "setembro",#30
        10: "outubro",#31
        11: "novembro",#30
        12: "dezembro"#31
    }
    if mes > 0 and mes <=12:
        if mes == 1 or  mes == 3  or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:   
            if dia > 0 and dia <=31:
                return f"{dia:02d} de {meses[mes]} de {ano}"
            else:
                return "Data Invalida"
        elif  mes == 4  or mes == 6 or mes == 9 or mes == 11:
            if dia > 0 and dia <=30:
                return f"{dia:02d} de {meses[mes]} de {ano}"
            else:
                return "Data Invalida"
        elif mes == 2:
            if dia > 0 and dia <=28:
                return f"{dia:02d} de {meses[mes]} de {ano}"
            else:
                return "Data Invalida"
    else: 
        return "Data Invalida"


diaa, mes, ano = map(int,input().split("/"))
dia(diaa, mes, ano)
print(dia(diaa, mes, ano))