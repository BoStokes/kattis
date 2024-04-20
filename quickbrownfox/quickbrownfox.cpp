#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        bool letters[26] = {0};

        string s;
        getline(cin, s);
        int used = 0;
        for (auto c : s) {
            int index = tolower(c) - 'a';
            if (index >= 0 && index < 26 && !letters[index]) {
                letters[index] = true;
                used++;
            }
        }
        if (used == 26) {
            cout << "pangram" << endl;
        }
        else {
            cout << "missing ";
            for (int j = 0; j < 26; j++) {
                if (!letters[j]) {
                    cout << (char)(j+'a');
                }
            }
            cout << endl;
        }
    } 
}