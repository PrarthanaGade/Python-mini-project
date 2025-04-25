//Creates an output file, writes information toi, closes the file and open it again as an input file and read info from the file

//Program 

#include <iostream>
#include <fstream>
using namespace std;

class Student {
public:
    int roll;
    char name[30];
    int marks;

    Student() {} // Default constructor

    void getdata();
    void displaydata();
};

void Student::getdata() {
    cout << "\nEnter Student Details -->" << endl;
    cout << "Enter roll no: ";
    cin >> roll;
    cin.ignore(); // Clear the input buffer
    cout << "Enter student name: ";
    cin.getline(name, 30);
    cout << "Enter marks: ";
    cin >> marks;
}

void Student::displaydata() {
    cout << "\nRoll No: " << roll << endl;
    cout << "Student's name: " << name << endl;
    cout << "Student's marks: " << marks << endl;
}

int main() {
    Student s[70];
    fstream file;
    int n;

    // Open file for output
    file.open("C:\\Users\\prart\\Desktop\\Python Mini projects\\xyx.txt", ios::out);
    if (!file) {
        cout << "Error in creating file!" << endl;
        return 1;
    }

    cout << "Enter Number of Students: ";
    cin >> n;

    // Write student data to the file
    for (int i = 0; i < n; i++) {
        s[i].getdata();
        file.write((char*)&s[i], sizeof(s[i]));
    }

    file.close();

    // Open file for input
    file.open("C:\\Users\\prart\\Desktop\\Python Mini projects\\xyx.txt", ios::in);
    if (!file) {
        cout << "Error in opening file for reading!" << endl;
        return 1;
    }

    cout << "\nReading student information from the file..." << endl;

    // Read student data from the file
    for (int i = 0; i < n; i++) {
        file.read((char*)&s[i], sizeof(s[i]));
        s[i].displaydata();
    }

    file.close();

    cout << "All operations completed successfully." << endl;
    return 0;
}
