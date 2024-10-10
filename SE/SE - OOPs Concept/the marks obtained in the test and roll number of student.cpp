#include<iostream>
using namespace std;

class Students {
   public:
    int roll_number;
};

class Test : public Students {
   public:
    int subject1_marks;
    int subject2_marks;
};

class Result : public Test {
   public:
    int total_marks() {
        return subject1_marks + subject2_marks;
    }
};

int main() {
    Result r;
    r.roll_number = 1;
    r.subject1_marks = 80;
    r.subject2_marks = 90;
    cout << "Roll Number: " << r.roll_number << endl;
    cout << "Total Marks: " << r.total_marks() << endl;
}

