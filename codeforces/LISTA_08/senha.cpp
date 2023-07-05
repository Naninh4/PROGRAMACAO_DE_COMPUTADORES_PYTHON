#include <iostream>
 
using namespace std;
 
int main()
{
    int senha =  9842, tentativa;
    while (true){
        std::cin >> tentativa;
        if (tentativa == senha){
            std:: cout << "Acesso Permitido." << std::endl;
            break;
        }else{
            std::cout << "Senha Invalida!" << std::endl;
            
        }
    }
    return 0;
}