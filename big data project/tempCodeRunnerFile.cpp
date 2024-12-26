#include <iostream>
#include <string.h>
using namespace std;

class myclass {
private:
    int a;
    static double d;
    char ch;

public:
    myclass(double h, int val, char c) {
        d = h + val;
        ch = c;
        a = (2*(int)d-2) % 3;
    
    }
    void show() {
        cout<<d<<'\t'<<a+3<<'\t'<<ch<<endl;
    }
    void showval() {
        cout<<ch<<'\t'<<2 - d/3<<'\t'<<a<<'\n';
    }

    myclass a_func(myclass obj) {
        myclass abc(3.2, 5, 'G');
        abc.d = d + obj.a;
        abc.ch = obj.ch;
        abc.a = int (d - obj.d-a);
        return myclass(d, a, ch);
    }
    myclass operator--() {
        double j = d++;
        int k = --a;
        char c = 'N';
        k++;
        --a;
        return myclass(d,k,c);
    }
    double b_function() {
        return a + d;
    }
};
double myclass::d = 0;


int main() {
    myclass obj1(3.1, 2, 'F'), obj2(1.3, 3, 'C');
    obj1 = obj1.a_func(obj2);
    obj2.show();
    obj1.showval();
    --obj2;
    obj2.showval();
    cout<<obj1.b_function()<<endl;
    return 0;
}


