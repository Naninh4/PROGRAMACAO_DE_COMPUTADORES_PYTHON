#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string DNA;
    vector<char> bases = {'A', 'C', 'G', 'T'};
    int maior = 0, cont = 0;

    cin >> DNA;

    for (int j = 0; j < bases.size(); j++) {
        for (int i = 0; i < DNA.size(); i++) {
            if (bases[j] == 'A' && DNA[i] == 'A') {
                cont++;
            } else if (bases[j] == 'C' && DNA[i] == 'C') {
                cont++;
            } else if (bases[j] == 'G' && DNA[i] == 'G') {
                cont++;
            } else if (bases[j] == 'T' && DNA[i] == 'T') {
                cont++;
            } else {
                if (cont > maior) {
                    maior = cont;
                }
                cont = 0;
            }
        }
        if (cont > maior) {
            maior = cont;
        }
        cont = 0;
    }
    cout << maior << endl;

    return 0;
}
