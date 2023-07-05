#include <iostream>
#include <iomanip>
 
int main()
{
    int mergulharam=0, voltaram= 0, dif = 0;
    std::cin >> mergulharam >> voltaram;
    
    int m_volt[voltaram];
    m_volt[0] = 0;
    for (int i = 0; i < voltaram; i++){
        std::cin >> m_volt[i];
    }
    
    if (mergulharam == voltaram){
        std::cout << "*"  << std::endl;
    }else{
        for(int x=1;x<=mergulharam;x++){
            for(int j = 0; j < voltaram;j++){
                if(x != m_volt[j]){
                    dif++;
                }
            }
            if (dif == voltaram){
                std::cout << x << " ";
                dif=0;
            }else{
                dif=0;
            }
            
        }
            
    }
    
    return 0;
}