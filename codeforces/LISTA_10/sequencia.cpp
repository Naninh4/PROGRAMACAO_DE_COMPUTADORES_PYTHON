#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    
    long long tm_sa, tm_sb;
    vector<long long> SA, SB, posicoes;

    cin >> tm_sa >>  tm_sb;
    SA.resize(tm_sa);
    SB.resize(tm_sb);
    for(int j=0;j<tm_sa;j++) cin >> SA[j];

    for(int i=0;i<tm_sb;i++){ 
        cin >> SB[i];
    }
    int j=0, i=0, aux=0;
    while(i<tm_sb){
        while(j < tm_sa){
             if(SB[i] == SA[j]){
                aux++;
                j++;
                j=j;
                i++;
                break;
            }
            j++;
        }
        if(tm_sa == j) break;
    }
    if(aux == SB.size()){
            cout << "S";
    }else{
            cout << "N";
    }
   

    return 0;
}
