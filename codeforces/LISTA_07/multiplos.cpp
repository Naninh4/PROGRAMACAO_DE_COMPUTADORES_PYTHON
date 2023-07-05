#include <iostream>
 
using namespace std;
 
int main()
{
    int qtd_caixas, aux;
    std::cin >> qtd_caixas;
    int* caixas = new int[qtd_caixas]; // Alocação dinâmica de memória
    
    int maiorp = 100, pontos=100;
    for (int x = 0; x < qtd_caixas; x++){
        std::cin >> aux;
        pontos = pontos + aux;
        if (pontos >= maiorp){
            maiorp = pontos;
        }
    }
    std::cout << (maiorp) << std::endl;

    delete[] caixas; // Liberação da memória alocada

    return 0;
}