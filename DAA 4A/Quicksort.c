#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Partition function (Lomuto partition scheme)
int partition(int A[], int p, int r) {
    int x = A[r];  // Pivot element
    int i = p - 1;  // Index of smaller element

    for (int j = p; j < r; j++) {
        if (A[j] <= x) {
            i++;
            swap(&A[i], &A[j]);
        }
    }

    swap(&A[i + 1], &A[r]);
    return i + 1;
}

// QuickSort function
void quickSort(int A[], int p, int r) {
    if (p < r) {
        int q = partition(A, p, r);
        quickSort(A, p, q - 1);
        quickSort(A, q + 1, r);
    }
}

// Function to print an array
void printArray(int A[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

// Main function
int main() {
    int n;

    // Asking for array size
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int A[n];  // Declare array of size n

    // Asking for array elements
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    printf("Original array: ");
    printArray(A, n);

    // Sorting the array using QuickSort
    quickSort(A, 0, n - 1);

    printf("Sorted array: ");
    printArray(A, n);

    return 0;
}
