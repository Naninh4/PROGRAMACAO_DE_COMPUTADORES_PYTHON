#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<float, int> a, pair<float, int> b){
    if (a.first!= b.first){
        return a.first>b.first;
    }else{
        return a.second<b.second;
    }

}

int main() {
    int N; // Quantidade de dígitos da senha
    int caso = 1; // Número do caso de teste
    
    
    while (cin >> N) {
        
        vector<pair<float, int>> teclas; // Vetor para armazenar os valores de óleo e seus índices

        for (int i = 0; i < 10; i++) {
            float oleo;
            cin >> oleo;
            teclas.push_back(make_pair(oleo, i));
        }
        
        stable_sort(teclas.begin(),teclas.end(), compare); // Ordena o vetor em ordem decrescente de óleo ESTÁVEL
        
        cout << "Caso " << caso << ": ";
        
        for (int i = 0; i < N; i++) {
            cout << teclas[i].second;
        }
        
        cout << endl;
        
        caso++;
    }
    
    return 0;
}
