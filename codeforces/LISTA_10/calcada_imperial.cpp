#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(false); cin.tie(0);

    int tm_seq, ans=1;
    vector<int> seq;
    cin >> tm_seq;
    seq.resize(tm_seq);
    
   	for(int i = 1; i <= tm_seq; i++) cin>>seq[i];

	for(int i = 1; i <= tm_seq; i++)
	{
		for(int j = 1; j <= tm_seq; j++)
		{
			if(seq[i] == seq[j]) continue;

			vector<int> seq_dif(2);

			seq_dif[0] = seq[i], seq_dif[1] = seq[j];
            // se são diferentes ele cria um vetor de duas posições com os dois numeros de seq
            // cout << seq_dif[0] << "  " << seq_dif[1] <<  endl;
			int zu = 0, cont = 0;

			for(int t = 1; t <= tm_seq; t++)
			{
				if(seq[t] == seq_dif[zu]) // set[t] == seq_dif[0] se sim ele avança uma posição em seq_dif e testa se o proximo numero é igual a seq_dif da posiçã
				// [1] se não for a posição se mantem [0] e seq[t] será testada com ela.
				{                
					zu ^= 1; // alternando entre posição 0 e posição 1.
					cont ++;
				}
			}
			ans = max(ans, cont);
		}
	}

    
    cout << ans <<  endl;
    
   
    return 0;
}