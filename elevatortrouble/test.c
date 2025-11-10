#include <stdio.h>

int main()
{
    int arr[1000000] = {0};

    for (int i = 0; i < 1000000; i++) {
        if (arr[i] != 0) {
            printf("error\n");
            break;
        }
    }
    printf("%d\n", arr[999245]);
}