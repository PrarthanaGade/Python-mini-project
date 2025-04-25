#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    string name;
    int pop;
    string states[] = {"Maharashtra", "Bihar", "Uttar Pradesh"};
    int pops[] = {111239, 112399, 123993};

    map<string, int> mapStates;

    // Populate the map with states and their populations
    for (int j = 0; j < 3; j++) { // Fixed loop syntax
        name = states[j];
        pop = pops[j];
        mapStates[name] = pop;
    }

    // Search for a state
    cout << "Enter state: ";
    cin >> name;

    if (mapStates.find(name) != mapStates.end()) { // Fixed syntax for comparison
        pop = mapStates[name]; // Fixed typo (mapState -> mapStates)
        cout << "Population: " << pop << "\n";
    } else {
        cout << "State not found!\n";
    }
    cout << endl;

    // Display all states and their populations
    for (const auto& iter : mapStates) {
        cout << iter.first << " : " << iter.second << "\n";
    }

    return 0;
}
