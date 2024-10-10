#include <iostream>
using namespace std;
class student
   {
      protected:
         int roll_number;
      public:
         void get_number(int);
         void put_number(void);
   };

void student :: get_number(int a)
   {
      roll_number = a;
   }

void student :: put_number()
   {
      cout << "Roll Number: " << roll_number << endl;
   }

class test : public student      //First level derivation
   {
      protected:
         float sub1;
         float sub2;
      public:
         void get_marks(float, float);
         void put_marks(void);
   };

void test :: get_marks(float x, float y)
   {
      sub1 = x;
      sub2 = y;
   }

void test :: put_marks()
   {
      cout << "Marks in Sub1 = " << sub1 << endl;
      cout << "Marks in Sub2 = " << sub2 << endl;
   }

class result : public test   //second Level Derivation
   {
         float total;      //private by default
      public:
         void display();
   };
using namespace std;

class Cricketer {
public:
    string name;
    int totalRuns, avgRuns, bestPerformance, numMatches;

    void inputData() {
        cout << "Enter name: " << endl;
        cin >> name;

        cout << "Enter total runs: " << endl;
        cin >> totalRuns;

        cout << "Enter no. of matches played: " << endl;
        cin >> numMatches;

        cout << "Enter best score: " << endl;
        cin >> bestPerformance;
    }

    void calAvg() {
        avgRuns = totalRuns / numMatches;
        cout << "Average: " << avgRuns << endl << endl;
    }
};

class Batsman : public Cricketer {
public:
    void display() {
        cout << "Name: " << name << endl;
        cout << "Total runs: " << totalRuns << endl;
        cout << "Best score: " << bestPerformance << endl;
        cout << "Average: " << avgRuns << endl;
    }
};

int main() {
    Batsman Player1;
    Player1.inputData();
    Player1.calAvg();
    Player1.display();
}
