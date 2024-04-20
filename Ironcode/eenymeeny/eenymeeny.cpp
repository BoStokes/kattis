#include <iostream>
#include <string>
#include <vector>

using namespace std;

int const num_words(string &line) {
    int words = 1;
    for (char c : line) {
        if (c == ' ') words++;
    }
    return words;
}

int main() {
    string line;
    getline(cin, line);
    int words = num_words(line);

    int n;
    cin >> n;
    vector<string> names;
    int used[n];
    for (int i = 0 ; i < n; i++) {
        cin >> line;
        names.push_back(line);
        used[i] = false;
    }
    vector<string> team1, team2;
    bool isTeam1 = true;

    for (int i = 0, count = 1; team1.size() + team2.size() != names.size(); i++) {
        if (used[i%n])
            continue;
        if (count % words == 0) {
            if (isTeam1)
                team1.push_back(names[i%n]);
            else
                team2.push_back(names[i%n]);
            used[i%n] = true;
            isTeam1 = ! isTeam1;
        }
        count++;
    }

    cout << team1.size() << '\n';
    for (string name : team1) {
        cout << name << '\n';
    }
    cout << team2.size() << '\n';
    for (string name : team2) {
        cout << name << '\n';
    }
}