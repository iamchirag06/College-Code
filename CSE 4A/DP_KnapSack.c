#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int n, m;

    printf("Enter the number of items: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Invalid number of items!\n");
        return 1;
    }

    printf("Enter the capacity of the knapsack: ");
    scanf("%d", &m);

    if (m <= 0) {
        printf("Invalid knapsack capacity!\n");
        return 1;
    }

    int p[n], w[n], k[n+1][m+1];

    // Input profits and weights
    for (int i = 0; i < n; i++) {
        printf("Profit[%d]: ", i + 1);
        scanf("%d", &p[i]);
        printf("Weight[%d]: ", i + 1);
        scanf("%d", &w[i]);

        if (w[i] <= 0) {
            printf("Invalid weight value!\n");
            return 1;
        }
    }

    // DP Table Construction
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (i == 0 || j == 0)
                k[i][j] = 0;
            else if (w[i-1] <= j)
                k[i][j] = max(p[i-1] + k[i-1][j - w[i-1]], k[i-1][j]);
            else
                k[i][j] = k[i-1][j];
        }
    }

    // Print DP Matrix
    printf("\nDP Matrix:\n");
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            printf("%d\t", k[i][j]);
        }
        printf("\n");
    }

    printf("\nMaximum profit is %d\n", k[n][m]);

    // Traceback to find selected items
    printf("Selected items: ");
    int i = n, j = m;
    int first = 1;
    
    while (i > 0 && j > 0) {
        if (k[i][j] != k[i-1][j]) {
            if (!first) printf(", ");
            printf("%d", i);
            first = 0;
            j -= w[i-1];
        }
        i--;
    }
    printf("\n");

    return 0;
}
