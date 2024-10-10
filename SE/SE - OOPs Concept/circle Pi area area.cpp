#include <iostream>
using namespace std;

int main() {
   float radius, areacircle;
   const float pi = 3.14159;

   cout << "Enter the radius of the circle: ";
   cin >> radius;

   areacircle = pi * radius * radius;

   cout << "Area of the circle: " << areacircle << endl;
}

