# 14. Escreva uma função recursiva que receba uma string s e retorne se a mesma é um palíndromo.
# Um palíndromo é um texto que possui a mesma sequencia de letras tanto lido da esquerda
# para a direita como da direita para a esquerda. Exemplo: abba é um palíndromo, enquanto
# abab não é. .
# Assinatura da função: def palindromo(s):
# OBS: Para este problema considere que a string já foi tratada e só contém letras minúsculas,
# sem acentos, sem pontuação e sem espaços.

def palindromo(s,cont1=0,cont=-1,igual=0):
    if cont1 == (len(s) -1) and cont == (len(s)*-1):
        if s[cont1] == s[cont]:
            igual+=1
        if igual == len(s):
            print(igual)
            return True
        else:
            print(igual)
            return False
    if s[cont1] == s[cont]:
        igual+=1
        return palindromo(s, cont1+1, cont -1,igual)
    else:
        return palindromo(s, cont1+1, cont -1,igual)

s = "123454321"
list(s)
print(palindromo(s))
