for x in range(int(input())):
    qtd_carneirinhos = int(input())
    carneirinhos = list(map(int,input().split()))
    if len(carneirinhos) == list(set(carneirinhos)):
        print(qtd_carneirinhos)
    else:
        print(len(list(set(carneirinhos))))