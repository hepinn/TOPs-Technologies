#include <iostream>
using namespace std;
class Person {
    protected:
        string name;
        int age;
    public:
        void read() {
            cout << "Enter name: ";
            getline(cin, name);
            cout << "Enter age: ";
            cin >> age;
        }
        void write() {
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
        }
};

class Student : public Person {
    private:
        float percentage;
    public:
        void read() {
            Person::read();
            cout << "Enter percentage: ";
            cin >> percentage;
        }
        void write() {
            Person::write();
            cout << "Percentage: " << percentage << endl;
        }
};

class Teacher : public Person {
    private:
        float salary;
    public:
        void read() {
            Person::read();
            cout << "Enter salary: ";
            cin >> salary;
        }
        void write() {
            Person::write();
            cout << "Salary: " << salary << endl;
        }
};

int main() {
    Student s;
    Teacher t;

    cout << "Enter student details:\n";
    s.read();
    cout << "\nEnter teacher details:\n";
    t.read();

    cout << "\nStudent details:\n";
    s.write();
    cout << "\nTeacher details:\n";
    t.write();

}

