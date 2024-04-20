#include <iostream>
#include <string>

using namespace std;

int main() {
    int n; cin >> n;

    int towers = 1;
    int last, current;
    cin >> current;
    for (int i = 1; i < n; i++) {
        last = current;
        cin >> current;
        if (current > last)
            towers++;
    }
    cout << towers << endl;
}