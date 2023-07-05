#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;


int main(){
    int qtd_testes, lampadaA=false, lampadaB=false, interruptor;

    cin >> qtd_testes;

    for(int x = 0; x<qtd_testes ;x++){
        cin >> interruptor;
        if (interruptor == 1){
            lampadaA = !lampadaA;
        }else{
            if(interruptor == 2) {
                lampadaB = !lampadaB;
                lampadaA = !lampadaA;
            }
        }
    }
    if(lampadaA==true){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }
    if(lampadaB==true){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }

    return 0;
}