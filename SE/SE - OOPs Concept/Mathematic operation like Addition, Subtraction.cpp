#include<iostream>
using namespace std;

class MathOperations {
    public:
        int add(int a, int b) {
            return a + b;
        }
        int subtract(int a, int b) {
            return a - b;
        }
        int multiply(int a, int b) {
            return a * b;
        }
        float divide(float a, float b) {
            return a / b;
        }
        int add(int a, int b, int c) {
            return a + b + c;
        }
};

int main() {
    MathOperations math;
    int a = 10, b = 5, c = 2;
    float d = 10.0, e = 2.0;

    cout << "Addition of " << a << " and " << b << " is " << math.add(a, b) << endl;
    cout << "Subtraction of " << a << " and " << b << " is " << math.subtract(a, b) << endl;
    cout << "Multiplication of " << a << " and " << b << " is " << math.multiply(a, b) << endl;
    cout << "Division of " << d << " and " << e << " is " << math.divide(d, e) << endl;
    cout << "Addition of " << a << ", " << b << " and " << c << " is " << math.add(a, b, c) << endl;

    return 0;
}
