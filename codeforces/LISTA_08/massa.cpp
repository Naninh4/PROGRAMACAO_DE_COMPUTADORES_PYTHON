#include <iostream>
#include <iomanip>
 
int main()
{
    long long tempoS=0,tempo = 0;
    double massaI = 0.0;
    std::cin >> tempoS >> massaI;

    while(massaI >=0.5){
        massaI = massaI / 2;
        tempo = tempo + tempoS;
    }

    int dias = tempo / (24 * 3600);  
    tempo %= (24 * 3600);  

    int horas = tempo / 3600;  
    tempo %= 3600;  

    int minutos = tempo / 60;  
    
    int segundos = tempo % 60;  
    
    std::cout << dias << " dias ";
    std::cout << std::setw(2) << std::setfill('0') << horas << ":";
    std::cout << std::setw(2) << std::setfill('0') << minutos << ":";
    std::cout << std::setw(2) << std::setfill('0') << segundos << std::endl;

    return 0;
}