#include <bits/stdc++.h>
using namespace std;

int main() {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pair<int, int> p1 {3, 3};
    pair<int, int> p2 {4, 4};
    pair<int, int> p3 {5, 4};
    pair<int, int> p4 {6, 4};
    pair<int, int> p5 {7, 4};
    pair<int, int> p6 {3, 1};

    pq.push(p1);
    pq.push(p2);
    pq.push(p3);
    pq.push(p4);
    pq.push(p5);
    pq.push(p6);

    for (int i = 0; i < 6; i++) {
        cout << pq.top().first << ' ' << pq.top().second << '\n';
        pq.pop();
    }
}