#include <iostream>
using namespace std;
int main(){
  int teste = 1, qtd_areas;
  while (true)
    {
      cin >> qtd_areas;
      if (!qtd_areas) break;

      cout << "Teste " << teste << endl;
      int x1 = -10000, y1 = 10000, 
        x2 = 10000, y2 = -10000;
      //pegando os parâmetros mais internos ou menores.
      while (qtd_areas > 0)
        {
          int a,b,c,d;
          cin >> a >> b >> c >> d;
          if (a > x1){
            x1 = a;
          } 
          if (b < y1){
             y1 = b;
          }
          if (c < x2){
             x2 = c;
          }
          if (d > y2){
             y2 = d;
          }
          qtd_areas --;
        }

      

      if (x2 < x1 || y1 < y2)
        cout << "nenhum" << endl;
      else{
        cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
      }
      cout << endl;
      teste ++;
    }
}

