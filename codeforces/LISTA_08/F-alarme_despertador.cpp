#include <iostream>
using namespace std;

int main (){
    int hora0, hora1, minuto0, minuto1, tempo0, tempo1;
 
    while (true) {
    	cin >> hora0 >> minuto0 >> hora1 >> minuto1;
    	
    	if (hora0==0 && hora1==0 && minuto0==0 && minuto1==0) { 
    		break; 
    	}
        
        tempo0 = (hora0 * 60) + minuto0;
        tempo1 = (hora1 * 60) + minuto1;
         
        if (tempo0 < tempo1){
        	cout << (tempo1-tempo0) << "\n";
        } else {
            cout << 1440+(tempo1-tempo0) << "\n";
        }
    }
 
    return 0;
}