#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    unordered_set<string> set;
    bool isPlayerOne = false;
    string lastWord, currentWord;
    cin >> currentWord;

    for (int i = 1; i < n; i++) {
        lastWord = currentWord;
        set.insert(lastWord);
        cin >> currentWord;

        if (set.count(currentWord) || lastWord.back() != currentWord.front()) {
            if (isPlayerOne)
                cout << "Player 1 lost" << endl;
            else
                cout << "Player 2 lost" << endl;
            return 0;
        }
        isPlayerOne = ! isPlayerOne;
    }
    cout << "Fair game" << endl;
}