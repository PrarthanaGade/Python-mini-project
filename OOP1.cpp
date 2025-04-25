#include <iostream>
using namespace std;

class complex {
private:
    int real;
    int img;

public:
    // Default constructor
    complex() : real(0), img(0) {}

    // Overloaded constructor to set values
    complex(int r, int i) : real(r), img(i) {}

    // Overloaded + operator
    complex operator+(const complex &other) {
        return complex(real + other.real, img + other.img);
    }

    // Overloaded * operator
    complex operator*(const complex &other) {
        return complex(real * other.real - img * other.img,
                       real * other.img + img * other.real);
    }

    // Friend functions for << and >>
    friend ostream &operator<<(ostream &output, const complex &c);
    friend istream &operator>>(istream &input, complex &c);
};

// Friend function definitions
ostream &operator<<(ostream &output, const complex &c) {
    output << c.real << "+" << c.img << "i";
    return output;
}

istream &operator>>(istream &input, complex &c) {
    cout << "Enter real part: ";
    input >> c.real;
    cout << "Enter imaginary part: ";
    input >> c.img;
    return input;
}

// Main function
int main() {
    complex c1, c2, sum, product;

    // Input two complex numbers
    cout << "Enter first complex number:\n";
    cin >> c1;
    cout << "First complex number: " << c1 << endl;

    cout << "Enter second complex number:\n";
    cin >> c2;
    cout << "Second complex number: " << c2 << endl;

    // Perform addition and multiplication
    sum = c1 + c2;
    product = c1 * c2;

    // Output results
    cout << "\nResults:\n";
    cout << "Addition: " << sum << endl;
    cout << "Multiplication: " << product << endl;

    return 0;
}
