#include<iostream>
using namespace std;
class Demo{
    public :
        int No1;
        int No2;
        Demo(int A=0,int B=0){
            cout<<"Inside Constructor\n";
            this->No1=A;
            this->No2=B;
        }
        ~Demo(){
            cout<<"Inside Desctructor\n";
        }
        void Display(){
            cout<<"Value of No1 is:"<<this->No1<<"\n";
            cout<<"Value of No2 is:"<<this->No2<<"\n";
        }

};
int main(){
    cout<<"Inside main\n";
    Demo dobj1;
    Demo dobj2(10,20);
    dobj1.Display();
    dobj2.Display();
    cout<<"End of main\n";

    return 0;

}