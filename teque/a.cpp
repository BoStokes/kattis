#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    deque<int> left;
    deque<int> right;
    int size = 0;

    string command;
    int num;
    for (int i = 0; i < n; i++) {
        cin >> command;
        cin >> num;
        if (command == "push_front") {
            left.push_front(num);
            size++;
        }
        else if (command == "push_back") {
            right.push_back(num);
            size++;
        }
        else if (command == "push_middle") {
            while (left.size() > right.size()) {
                right.push_front(left.back());
                left.pop_back();
            }
            while (right.size() > left.size()) {
                left.push_back(right.front());
                right.pop_front();
            }

            left.push_back(num);

            size++;
        }
        else {
            if (num < left.size()) {
                cout << left[num] << '\n';
            }
            else {
                cout << right[num - left.size()] << '\n';
            }
        }
    }
}