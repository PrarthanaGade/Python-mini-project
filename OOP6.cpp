//inheritance program
#include<iostream>
#include<string>
using namespace std;

//Books record

class Publication {
    protected:
      string: title;
      float: price;

    public:
      Publication() : title (" "), price (0.0) {}

      void getData(){
        cout<<"Enter title :";
        cin.ignore();
        getline(cin, title);
        cout << "Enter price: ";
        cin>> price;

        
      }
}