#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;


int main(){

    int num_jogadores, num_rodadas, jogada, maior=0, jogador_atual=0, anterior=0, x=1, index;

    vector<pair<int, int>> jogadas; // Vetor para armazenar os valores de óleo e seus índices


    cin >> num_jogadores >> num_rodadas;

    for(int x=1; x <= num_jogadores;x++){
        jogadas.push_back(make_pair(0, x));

    }
    for(int x=1; x < ((num_jogadores*num_rodadas)+1);x++){
        cin >> jogada;

        jogador_atual = x % num_jogadores;
        if (jogador_atual == 0){
            jogador_atual = anterior +1;
        }
    
        jogadas[jogador_atual-1].first += jogada;

        anterior = jogador_atual;
    }
    for (int a = 0; a< num_jogadores; a++){
        if (jogadas[a].first >= maior){
            maior = jogadas[a].first;
            index = jogadas[a].second;
        }
    }
    

    cout << index;
    return 0;
}