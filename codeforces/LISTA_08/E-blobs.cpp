#include <iostream>
using namespace std;

int main()
{

    int testes = 0, cont = 0;
    double caso = 0.0;

    cin >> testes;

    for(int x=0; x< testes;x++){

        cin >> caso;

        while(caso>1){

            caso /= 2;
            cont +=1;
        }
        
        cout << cont << " dias" << endl;
        cont = 0;
        
    }

    return 0;
}