#include <iostream>
using namespace std;

class Addition
{
private:
    float c;

public:
    Addition(float a, float b);
};

Addition::Addition(float a, float b)
{
    c = a + b;
    cout << "Sum of the given 2 number is:- " << c << endl;
}

class Subtraction
{
private:
    float c;

public:
    Subtraction(float a, float b);
};

Subtraction::Subtraction(float a, float b)
{
    c = a - b;
    cout << "Difference of the given 2 number is:- " << c << endl;
}

class Multiplication
{
private:
    float c;

public:
    Multiplication(float a, float b);
};

Multiplication::Multiplication(float a, float b)
{
    c = a * b;
    cout << "Product of the given 2 number is:- " << c << endl;
}

class Division
{
private:
    float c;

public:
    Division(float a, float b);
};

Division::Division(float a, float b)
{
    c = a / b;
    cout << "Division of the given 2 number is:- " << c << endl;
}

int main()
{
    system("cls");
    float x, y;
    cout << "Enter 2 numbers:-\n";
    cin >> x >> y;

    Addition add(x, y);
    Subtraction sub(x, y);
    Multiplication mult(x, y);
    Division div(x, y);

}
