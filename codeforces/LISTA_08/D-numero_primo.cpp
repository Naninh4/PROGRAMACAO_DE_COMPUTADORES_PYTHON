#include <iostream>

int primo(int num) {
    int divisores = 1;
    for (int i = 2; i <= (num / 2); i++) {
        if (num % i == 0) {
            divisores++;
        }
    }
    return divisores;
}

int main() {
    int star = 0;
    std::cin >> star;
    star++;
    while (true) {
        
        if (star % 2 == 0) {
            if (star == 2){
                std::cout << star << std::endl;
                break;
            }
            star++;
        } else {
            int divisores = primo(star);
            if (divisores == 1) {
                std::cout << star << std::endl;
                break;
            } else {
                star++;
            }
        }
    }
    return 0;
}
