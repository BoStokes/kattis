#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<string> vec;
    vec.push_back("");
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        vec.push_back(s);
    }
    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a;
        cin >> b;

        vec[a] += vec[b];
        vec[b] = "";
    }
    for (string s : vec) {
        if (s != "")
            cout << s << endl;
    }
}