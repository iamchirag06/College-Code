#include<stdio.h>

void swap(float a[], int i, int j) {
    float temp;
    temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

int main() {
    int i, j, m, n;
    float a[100], b[100], c[100];
    float p = 0.0; // Initialize profit to 0

    // Input number of objects and knapsack capacity
    printf("Enter the number of objects: ");
    scanf("%d", &n);
    printf("Enter the capacity of Knapsack: ");
    scanf("%d", &m);

    // Input profits of the objects
    printf("Enter the Profits of the objects:\n");
    for(i = 0; i < n; i++) {
        scanf("%f", &a[i]);
    }

    // Input weights of the objects
    printf("Enter the Weight of the objects:\n");
    for(i = 0; i < n; i++) {
        scanf("%f", &b[i]);
    }

    // Calculate profit/weight ratio
    for(i = 0; i < n; i++) {
        c[i] = a[i] / b[i];
    }

    // Sorting the items based on the profit/weight ratio
    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(c[i] < c[j]) {
                swap(c, i, j);
                swap(a, i, j);
                swap(b, i, j);
            }
        }
    }

    // Greedily pick items to maximize profit
    for(i = 0; i < n; i++) {
        if(m >= b[i]) { // If the item can be fully added
            m -= b[i];
            p += a[i];  // Add full profit
        } else { // If only a fraction of the item can be added
            p += a[i] * (m / b[i]);
            break; // The knapsack is full, exit the loop
        }
    }

    // Output the maximum profit
    printf("Maximum Profit is %.2f\n", p);

    return 0;
}
