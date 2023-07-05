#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;


int main(){

    string crib, palavra;
    int aux = 0;
    int posicoes =0;

    cin >> crib >> palavra;

    int tm_total = crib.size() - palavra.size();

    for( int a = 0;a<=tm_total;a++){
        aux=0;  
        for(int x = 0; x<palavra.size(); x++){
            if (palavra[x] != crib[x]){
                aux++;
            }
        }
        if (aux == palavra.size()) posicoes++;
        crib.erase(crib.begin());
        
    }

    cout << posicoes;
    cout << endl;
    return 0;
}