#include <iostream>

int main()
{
    int pulo = 0, numeroCanos = 0, altura = 0;
    bool deu = true;
    std::cin >> pulo >> numeroCanos;
    
    int lista[numeroCanos];
    for (int x = 0; x < numeroCanos; x++) {
        std::cin >> altura;
        lista[x] = altura;
    }
    
    int cont = 0;
    while (deu && cont < numeroCanos - 1) {
        if (abs(lista[cont] - lista[cont+1]) <= pulo) {
            cont++;
        } else {
            deu = false;
        }
    }
    
    if (!deu) {
        std::cout << "GAME OVER";
    } else {
        std::cout << "YOU WIN";
    }
    
    return 0;
}
