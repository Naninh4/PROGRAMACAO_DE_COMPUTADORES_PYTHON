terceiro_andar = int(input())

segundo_andar =int(input())

primeiro_andar = int(input())

minutos_primeiro_andar = (terceiro_andar * 4) + (segundo_andar * 2)

minutos_segundo_andar = (terceiro_andar * 2) + (primeiro_andar * 2)

minutos_terceiro_andar = (primeiro_andar * 4) + (segundo_andar * 2)
menor_tempo = [minutos_primeiro_andar, minutos_segundo_andar, minutos_terceiro_andar]

menor_tempo.sort()
print(menor_tempo[0])