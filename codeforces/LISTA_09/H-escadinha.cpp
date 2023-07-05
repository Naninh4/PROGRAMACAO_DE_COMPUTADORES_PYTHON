#include <iostream>
#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;

int main(){

    int seq_nums=0, qtd_escadas=0, dif, num=0;
    vector<int> escadinhas;
    cin >> seq_nums;

    for (int x = 0; x < seq_nums; x++) {
        cin >> num;
        escadinhas.push_back(num);
    }
    if (escadinhas.size()==1){
        cout << 1;
    }else{
        dif = abs(escadinhas[-1] - escadinhas[-2]);
        for(int a=seq_nums; a>1; a--){
            if(abs(escadinhas[a-1] - escadinhas[a-2]) != dif){
                qtd_escadas ++;
                dif = abs(escadinhas[a-1] - escadinhas[a-2]);
            }
        }
            cout << qtd_escadas;   
    }
    return 0;
}