#include <stdio.h>

int main() {
    int c;
    scanf("%d", &c);

    int n;
    for (int i = 0; i < c; i++) {
        scanf("%d", &n);
        int total = 0;
        float avg = 0.0;
        int students[n];
        for (int j = 0; j < n; j++) {
            scanf("%d", &students[j]);
            total += students[j];
        }
        avg = (float)total / n;
        int num = 0;
        for (int j = 0; j < n; j++) {
            if (students[j] > avg) {
                num++;
            }
        }
        printf("%.3f%%\n", 100 * (float)num / n);
    }
}