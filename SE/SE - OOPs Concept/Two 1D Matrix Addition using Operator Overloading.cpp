#include<iostream>
using namespace std;

class Matrix {
    int a[100];
    int n;
public:
    Matrix(int n) {
        this->n = n;
        for (int i = 0; i < n; i++) {
            a[i] = 0;
        }
    }

    void input() {
        cout << "Enter the elements of the matrix: ";
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
    }

    Matrix operator+(Matrix m) {
        Matrix temp(n);
        for (int i = 0; i < n; i++) {
            temp.a[i] = a[i] + m.a[i];
        }
        return temp;
    }

    void display() {
        cout << "The sum of the matrices is: ";
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    int n;
    cout << "Enter the size of the matrix: ";
    cin >> n;
    Matrix m1(n), m2(n), m3(n);
    m1.input();
    m2.input();
    m3 = m1 + m2;
    m3.display();
    
}
