#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tamanho, menor=1000000, perder=0, ganhar=0;
    cin >> tamanho;
    int escada[tamanho];
    
    for( int x=0; x<tamanho;x++){
        int degrau;
        cin >> degrau;
        escada[x] = degrau;
        if(degrau<menor){
            menor = degrau;
        }
    }
    
    
    for( int a=0; a<tamanho; a++){
        if(escada[a]>(menor+a)){
            perder += escada[a]-(menor+a);
        }
        if(escada[a]<(menor+a)){
            ganhar += (menor+a)-escada[a];
        }
    }
    if(ganhar==perder){
        cout << (ganhar);
    }else{
        cout << (-1);
    }
    
    return 0;
}