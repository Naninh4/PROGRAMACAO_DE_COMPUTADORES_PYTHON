#include <iostream>
using namespace std;
// getline(cin, variavel);
//cin.ignore();
int calcularSoma(int num) {
    int soma = 0;
    while (num > 0) {
        soma += num % 10;
        num /= 10;
    }
    return soma;
}

int main() {
    long long soma1 = 0, soma2 = 0;
    string num1, num2;
    while (true) {
        cin >> num1 >> num2;
        for (char c : num1) {
            soma1 += c - '0';
        }
        for (char c : num2) {
            soma2 += c - '0';
            // Na tabela aski o 0 equivale a 48(valor do caractere 0 - o valor do caractere c)
        }
        if (num1 == "0" || num2 == "0") {
            break;
        }
        while (soma1 > 9 || soma2 > 9) {
            if (soma1 > 9) {
                soma1 = calcularSoma(soma1);
            }
            if (soma2 > 9) {
                soma2 = calcularSoma(soma2);
            }
        }
        if( soma1 == soma2){
            cout << 0 << endl;
        }else if (soma1 >= soma2) {
            cout << 1 << endl;
        } else{
            cout << 2 << endl;
        }
        soma1 = 0;
        soma2 = 0;
    }
    return 0;
}
