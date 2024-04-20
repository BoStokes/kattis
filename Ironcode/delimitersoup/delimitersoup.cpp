#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;
    string line;
    cin.ignore();
    getline(cin, line);
    stack<char> stack;

    for (int i = 0; i < line.size(); i++) {
        char c = line[i];
        if (c == ' ') continue;

        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        }
        else if (c == ')') {
            if (stack.empty() || stack.top() != '(') {
                cout << ") " << i << endl;
                return 0;
            }
            stack.pop();
        }
        else if (c == ']') {
            if (stack.empty() || stack.top() != '[') {
                cout << "] " << i << endl;
                return 0;
            }
            stack.pop();
        }
        else if (c == '}') {
            if (stack.empty() || stack.top() != '{') {
                cout << "} " << i << endl;
                return 0;
            }
            stack.pop();
        }
    }
    cout << "ok so far" << endl;
}