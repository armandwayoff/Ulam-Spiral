#include <iostream>
#include <cmath>

using namespace std;

int move(int x) {
   return floor((sqrt(4 * x + 1) + 3) % 4 + 1);
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i < n; i++) {
         if (n % i == 0) return false;
    }
    return true;
}

int main()
{
   int spiralSize = 9;
   int centralNumber = 1;
   int matrix[spiralSize, spiralSize];

   int x, y = floor(spiralSize / 2);

   for (int n = centralNumber; n < spiralSize ** 2 + centralNumber; i++) {
      if (isPrime(n)) {
         matrix[y][x] = "0";
      } else {
         matrix[y][x] = "";
      }
      switch(move(n - centralNumber)) {
      case 1:
         x++;
         break;
      case 2:
         y--;
         break;
      case 3:
         x--;
         break;
      case 4:
         y++;
         break;
      }
   }

   for (int i = 0; i < spiralSize; i++) {
      cout << matrix[i];
   }

   return 0;
}
