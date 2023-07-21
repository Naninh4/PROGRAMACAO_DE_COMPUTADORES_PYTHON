#include <bits/stdc++.h>

using namespace std;

int main(){

    int tm_seq, cont=0;
    bool seqa = false;
    vector<int> seq, aux;

    while(cin >> tm_seq){
        seqa = false;
        cont =0;
        aux.clear();
        seq.resize(tm_seq);
        for(int x=0; x<tm_seq;x++){
            cin >>  seq[x];
        }
        for(int i = 1; i <seq.size(); i++){
                int o = 1;
		        for(o ; o <seq.size(); o++){
		          //  cout <<  seq[i] << "  " << seq[i-1] << "  " << o << endl;  
                    if((abs(seq[i] - seq[i-1]) == o)){
                        // cout <<  seq[i] << "  " << seq[i-1] << "  " << o << endl;
                        aux.push_back(o);
                        break;
                    }
		        }
                
        }
        for(int g=1;g<seq.size();g++){
            int a=0;
            for(a;a<aux.size();a++){
                // cout << g << "  " << aux[a] << endl;
                if(g == aux[a]){
                    seqa = true;
                    break;
                }else seqa = false;
            }
            if(seqa == false){
                cout <<  "Nao alegre" <<  endl;
                break;
            }else cont++;
        }
        if( cont==(seq.size()-1)){
            cout << "Alegre" << endl;
        }
    }
        


    return 0;
}