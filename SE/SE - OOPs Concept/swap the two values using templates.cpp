#include <iostream>
using namespace std;

template <typename T>
void swap_values(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 5, y = 10;
    cout << "Before swapping: x = " << x << ", y = " << y << endl;
    swap_values(x, y);
    cout << "After swapping: x = " << x << ", y = " << y << endl;
}

