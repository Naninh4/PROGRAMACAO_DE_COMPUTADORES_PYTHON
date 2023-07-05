#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;

int main(){
    int qtd_competidores, qtd_finalistas;
    vector<int> pontos;
    cin >> qtd_competidores >> qtd_finalistas;

    for(int x=0; x<qtd_competidores;x++){
        int ponto;
        cin >> ponto;
        pontos.push_back(ponto);
    }    
    sort(pontos.rbegin(), pontos.rend());
    int ultimo = pontos[qtd_finalistas-1];

    for(int a=qtd_finalistas; a<=qtd_competidores;a++){
        if (pontos[a] == ultimo){
            qtd_finalistas++;
        }
    }
    cout << qtd_finalistas;
}