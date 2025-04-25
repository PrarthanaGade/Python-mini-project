/*Create a user defined exception to check the following and throw the exception when needed.
 1) User has age between 18 to 55
 2)User stays has income between Rs 50,0000 - Rs 1,00,000 permonth
 3)User stays in pune /mumbai/banglore/chennai 
 4)User has four wheelers*/

#include <iostream>
#include <string>
using namespace std;

class Details {
    int age;
    int income;
    int vehicle;
    string city;

public:
    Details() {
        while (true) {
            try {
                cout << "Exception Handling!!" << endl;
                cout << "Enter age: ";
                cin >> age;

                if (age > 18 && age < 55) {
                    cout << "Access granted for age." << endl;
                    break;
                } else {
                    throw age;
                }
            } catch (int age) {
                cout << "You are not eligible due to age restrictions." << endl;
            }
        }

        while (true) {
            try {
                cout << "Exception Handling!!" << endl;
                cout << "Enter your monthly income: ";
                cin >> income;

                if (income > 50000 && income < 100000) {
                    cout << "Access granted for income." << endl;
                    break;
                } else {
                    throw income;
                }
            } catch (int income) {
                cout << "You are not eligible due to income restrictions." << endl;
            }
        }

        while (true) {
            try {
                cout << "Exception Handling!!" << endl;
                cout << "How many 4-wheelers do you have? ";
                cin >> vehicle;

                if (vehicle > 0) {
                    cout << "Access granted for vehicle ownership." << endl;
                    break;
                } else {
                    throw vehicle;
                }
            } catch (int vehicle) {
                cout << "You are not eligible due to vehicle ownership restrictions." << endl;
            }
        }

        while (true) {
            try {
                cout << "Exception Handling!!" << endl;
                cout << "Enter the city you live in: ";
                cin >> city;

                if (city == "pune" || city == "mumbai" || city == "banglore" || city == "chennai") {
                    cout << "Access granted for city." << endl;
                    break;
                } else {
                    throw city;
                }
            } catch (string city) {
                cout << "You are not eligible due to city restrictions." << endl;
            }
        }
    }
};

int main() {
    Details a;
    cout << "Thank you for showing your interest!" << endl;

    return 0;
}
