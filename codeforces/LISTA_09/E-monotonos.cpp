#include <iostream>
#include <vector>
using namespace std;

int main() {
    int size_string, qtd = 0;
    vector<char> varchar;
    char char_atual, char_anterior, char_penul;

    cin >> size_string;
    for (int x = 0; x < size_string; x++) {
        cin >> char_atual;
        varchar.push_back(char_atual);
    }
    
    for (int x = 0; x < varchar.size(); x++) {
        if(x==0){
            if (varchar[x] == 'a' && varchar[x+1] ==    'a') {
            qtd++;
            continue;
        }
        }
        if (varchar[x] == 'a' && (varchar[x+1] == 'a' || varchar[x-1] == 'a')) {
            qtd++;
        }
    }
    cout << qtd << endl;
    return 0;
}
