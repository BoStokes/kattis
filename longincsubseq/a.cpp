#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;

int n;
vi A, p;

void print_LIS(int i) {
    if (p[i] == -1) {
        printf("%d", i);
        return;
    }
    print_LIS(p[i]);
    printf(" %d", i);

}

int main() {
    while (cin >> n) {
        A.assign(n, 0);
        for (int i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        int k = 0, lis_end = 0;
        vi L(n, 0), L_idx(n, 0);
        p.assign(n, -1);

        for (int i = 0; i < n; i++) {
            int pos = lower_bound(L.begin(), L.begin()+k, A[i]) - L.begin();
            L[pos] = A[i];
            L_idx[pos] = i;
            p[i] = pos > 0 ? L_idx[pos-1] : -1;
            if (pos == k) {
                k++;
                lis_end = i;
            }
        }

        printf("%d\n", k);
        print_LIS(lis_end);
        printf("\n");
    }
}