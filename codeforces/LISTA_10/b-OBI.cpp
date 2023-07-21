#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(false); cin.tie(0);

    int casos, nota_corte, cont =0;
    cin >> casos >> nota_corte;
    
    for(int t=0; t<casos; t++){
        int p1, p2;
        cin >>  p1 >> p2;
        if(p1 + p2 >=nota_corte){
            cont++;
        }

    }
    cout <<  cont <<  endl;
    return 0;
}