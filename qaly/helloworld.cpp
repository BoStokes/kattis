#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    double total = 0;
    for (int i = 0; i < n; i++) {
        double quality, years;
        cin >> quality;
        cin >> years;
        total += quality * years;
    }
    cout << total << endl;
}