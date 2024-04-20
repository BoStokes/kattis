#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int num_squares, index, magic_num;
    cin >> num_squares >> index >> magic_num;
    index--;
    int board[num_squares];
    for (int i = 0; i < num_squares; i++) {
        cin >> board[i];
    }
    unordered_set<int> set;
    int hops = 0;
    while (set.insert(index).second && 0 <= index && index < num_squares && board[index] != magic_num) {
        index += board[index];
        hops++;
    }

    if (board[index] == magic_num) {
        cout << "magic\n";
    } else if (index < 0) {
        cout << "left\n";
    } else if (index >= num_squares) {
        cout << "right\n";
    } else {
        cout << "cycle\n";
    }
    cout << hops << endl;
}