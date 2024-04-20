#include <iostream>
#include <string>
using namespace std;

string encode(string &message) {
    string ans;
    int i = 0;
    while (i < message.length()) {
        char c = message[i++];
        int count = 1;
        while (i < message.length() && message[i] == c) {
            i++;
            count++;
        }
        ans += c + to_string(count);
    }
    return ans;
}
string decode(string &message) {
    string ans;
    int i = 0;
    while (i < message.length()) {
        char c = message[i++];
        int count = message[i++] - '0';
        while (count-- > 0) {
            ans += c;
        }
    }
    return ans;
}

int main() {
    char option;
    cin >> option;
    string message;
    cin >> message;

    if (option == 'E') {
        cout << encode(message) << endl;
    }
    else {
        cout << decode(message) << endl;
    }
}