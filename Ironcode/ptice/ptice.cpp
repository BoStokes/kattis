#include <iostream>
#include <string>

using namespace std;

int main() {
    string a = "ABC";
    string b = "BABC";
    string g = "CCAABB";
    int adrian = 0, bruno = 0, goran = 0;

    int N;
    cin >> N;
    string answers;
    cin >> answers;

    for (int i = 0; i < answers.size(); i++) {
        if (a[i%3] == answers[i])
            adrian++;
        if (b[i%4] == answers[i])
            bruno++;
        if (g[i%6] == answers[i])
            goran++;
    }

    int c = max(max(adrian, bruno), goran);
    cout << c << endl;
    if (adrian == c)
        cout << "Adrian\n";
    if (bruno == c)
        cout << "Bruno\n";
    if (goran == c) 
        cout << "Goran\n";
}