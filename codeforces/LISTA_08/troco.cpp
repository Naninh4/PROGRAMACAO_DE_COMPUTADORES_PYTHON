#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int testes = 0;
    int total = 0, qtd_marcas = 0;
    double aux = 0.0, valor_u = 0.0, maior = 0.0;
    bool entrou = false;
    vector<double> trocos;

    cin >> testes;
    for (int x = 0; x < testes; x++) {
        cin >> total >> qtd_marcas;
        for (int a = 0; a < qtd_marcas; a++) {
            cin >> valor_u;
            if (valor_u<=total){
                aux = total;
            }else{
                aux = 0.0;
            }
            while (aux >= valor_u) {
                aux = aux - valor_u;
            }
            trocos.push_back(aux);
        }
        for (int p = 0; p < trocos.size(); p++) {
            if (trocos[p] > maior) {
                maior = trocos[p];
            }
        }
        cout << fixed << setprecision(2) << maior << endl;
        maior = 0;
        trocos.clear();
    }

    return 0;
}
