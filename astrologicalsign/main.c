#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);

    int day;
    char month[4];
    while (t-- > 0) {
        scanf("%d", &day);
        scanf("%s\n", month);
        if (strcmp(month, "Mar") == 0 && day >= 21 || strcmp(month, "Apr") == 0 && day <= 20) {
            printf("Aries\n");
        }
        else if (strcmp(month, "Apr") == 0 && day >= 21 || strcmp(month, "May") == 0 && day <= 20) {
            printf("Taurus\n");
        }
        else if (strcmp(month, "May") == 0 && day >= 21 || strcmp(month, "Jun") == 0 && day <= 21) {
            printf("Gemini\n");
        }
        else if (strcmp(month, "Jun") == 0 && day >= 22 || strcmp(month, "Jul") == 0 && day <= 22) {
            printf("Cancer\n");
        }
        else if (strcmp(month, "Jul") == 0 && day >= 23 || strcmp(month, "Aug") == 0 && day <= 22) {
            printf("Leo\n");
        }
        else if (strcmp(month, "Aug") == 0 && day >= 23 || strcmp(month, "Sep") == 0 && day <= 21) {
            printf("Virgo\n");
        }
        else if (strcmp(month, "Sep") == 0 && day >= 22 || strcmp(month, "Oct") == 0 && day <= 22) {
            printf("Libra\n");
        }
        else if (strcmp(month, "Oct") == 0 && day >= 23 || strcmp(month, "Nov") == 0 && day <= 22) {
            printf("Scorpio\n");
        }
        else if (strcmp(month, "Nov") == 0 && day >= 23 || strcmp(month, "Dec") == 0 && day <= 21) {
            printf("Sagittarius\n");
        }
        else if (strcmp(month, "Dec") == 0 && day >= 22 || strcmp(month, "Jan") == 0 && day <= 20) {
            printf("Capricorn\n");
        }
        else if (strcmp(month, "Jan") == 0 && day >= 21 || strcmp(month, "Feb") == 0 && day <= 19) {
            printf("Aquarius\n");
        }
        else if (strcmp(month, "Feb") == 0 && day >= 20 || strcmp(month, "Mar") == 0 && day <= 20) {
            printf("Pisces\n");
        }
    }
}