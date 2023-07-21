#include <bits/stdc++.h> // importa toda biblioteca padrão do c++ USAR EM COMPETIÇÃO
using namespace std;
 
 
int main(){
 
    string crib, palavra;
    int aux = 0;
 
    vector<char> cribList, palavraList;
 
    int posicoes =0;
 
    cin >> crib >> palavra;
 
    for (char c : crib) {
        cribList.push_back(c);
    }
    for (char c : palavra) {
        palavraList.push_back(c);
    }
 
    for( int a = 0;a<cribList.size();a++){
        for(int x = 0; x<palavraList.size(); x++){
            if (palavraList[x] != cribList[x]){
                aux++;
            }
//verme
        }
        if (aux == palavraList.size()) posicoes++;
        aux=0;
 
        if (cribList.size()==palavraList.size()){
            break;
        }else{
            cribList.erase(cribList.begin());
            a=0;
        }
        
    }
    
 
    cout << posicoes;
    return 0;
}