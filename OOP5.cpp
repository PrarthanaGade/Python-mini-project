#include <bits/stdc++.h>
using namespace std;

struct Record {
    string name;
    string dob;
    string telephone;
};

// Comparator function to sort records by name
bool compareRecords(const Record& a, const Record& b) {
    return a.name < b.name;
}

int main() {
    vector<Record> Records; // Vector to store records
    int n;

    cout << "Enter the number of personal records: ";
    cin >> n;

    // Input records
    for (int i = 0; i < n; i++) {
        Record record;
        cout << "Enter name: ";
        cin >> record.name;
        cout << "Enter DOB (dd-mm-yyyy): ";
        cin >> record.dob;
        cout << "Enter telephone number: ";
        cin >> record.telephone;
        Records.push_back(record); // Store the record in the vector
    }

    // Sort records by name
    sort(Records.begin(), Records.end(), compareRecords);

    // Display sorted records
    cout << "\nSorted personal records:\n";
    for (const Record& record : Records) {
        cout << "Name: " << record.name 
             << ", DOB: " << record.dob 
             << ", Telephone Number: " << record.telephone << endl;
    }

    // Search for a specific record by name
    string searchName;
    cout << "\nEnter name to search: ";
    cin >> searchName;

    auto it = find_if(Records.begin(), Records.end(), [&searchName](const Record& record) {
        return record.name == searchName;
    });

    if (it != Records.end()) {
        // Record found
        cout << "\nRecord found:\n";
        cout << "Name: " << it->name 
             << ", DOB: " << it->dob 
             << ", Telephone Number: " << it->telephone << endl;
    } else {
        // Record not found
        cout << "\nRecord with name '" << searchName << "' not found." << endl;
    }

    return 0;
}
