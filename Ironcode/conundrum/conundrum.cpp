#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;
    cin >> message;

    int count = 0;
    for (auto i = 0; i < message.length(); i++) {
        if (i % 3 == 0 && message[i] != 'P')
            count++;
        else if (i % 3 == 1 && message[i] != 'E')
            count++;
        else if (i % 3 == 2 && message[i] != 'R')
            count++;
    }
    cout << count << endl;
}