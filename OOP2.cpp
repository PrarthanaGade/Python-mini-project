//Write a C++ program create a calculator for an arithmathic operator (*/+/-/). 
//The program should take two operands from user and performs the operation on those two operator
//Use the switch statement to select the operation
//Finally display, the result

//Program

#include <iostream>
using namespace std;

class Calculator {
public:
    // Function for addition
    float add(float a, float b) {
        return a + b;
    }

    // Function for subtraction
    float sub(float a, float b) {
        return a - b;
    }

    // Function for multiplication
    float mul(float a, float b) {
        return a * b;
    }

    // Function for division
    float div(float a, float b) {
        if (b == 0) {
            cout << "Error: Division by zero is not possible." << endl;
            return 0;  // Return a default value to handle division by zero
        }
        return a / b;
    }
};

int main() {
    Calculator calc;
    char op;
    float num1, num2, result;
    char choice;

    do {
        // Take input from the user
        cout << "Enter the first number: ";
        cin >> num1;
        cout << "Enter the second number: ";
        cin >> num2;
        cout << "Enter the operator (+, -, *, /): ";
        cin >> op;

        // Perform operation based on user input
        switch (op) {
            case '+':
                result = calc.add(num1, num2);
                break;
            case '-':
                result = calc.sub(num1, num2);
                break;
            case '*':
                result = calc.mul(num1, num2);
                break;
            case '/':
                result = calc.div(num1, num2);
                break;
            default:
                cout << "Error: Invalid operator!" << endl;
                continue;
        }

        // Display the result
        cout << "Result: " << result << endl;

        // Ask if the user wants to perform another calculation
        cout << "Do you want to perform another calculation? (y/n): ";
        cin >> choice;

    } while (choice == 'y' || choice == 'Y');

    cout << "Thanks, goodbye!" << endl;

    return 0;
}

