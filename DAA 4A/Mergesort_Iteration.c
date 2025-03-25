#include<stdio.h>
#include<stdlib.h>

// Print Array
void printArray(int Array[], int size){
    for (int i = 0; i < size; i++){
        printf("%d\t", Array[i]);
    }
    printf("\n");
}

// Merge two arrays
void merge(int Arr[], int l, int mid, int r){
    int n1 = mid - l + 1;
    int n2 = r - mid;

    int A[n1], B[n2];

    for(int i = 0; i < n1; i++){
        A[i] = Arr[l + i];
    }
    for(int i = 0; i < n2; i++){
        B[i] = Arr[mid + 1 + i];
    }

    int i = 0, j = 0, k = l;
    while(i < n1 && j < n2){
        if(A[i] < B[j]){
            Arr[k] = A[i];
            i++;
        }
        else{
            Arr[k] = B[j];
            j++;
        }
        k++;
    }

    while(i < n1){
        Arr[k] = A[i];
        i++; k++;
    }
    while(j < n2){
        Arr[k] = B[j];
        j++; k++;
    }
}

// Iterative Merge Sort
void mergeSort(int Arr[], int size){
    int curr_size;
    int left_start;

    for (curr_size = 1; curr_size < size; curr_size *= 2){
        for (left_start = 0; left_start < size - 1; left_start += 2 * curr_size){
            int mid = left_start + curr_size - 1;
            int right_end = (left_start + 2 * curr_size - 1 < size - 1) ? (left_start + 2 * curr_size - 1) : (size - 1);
            merge(Arr, left_start, mid, right_end);
        }
    }
}

int main(){
    int size;
    printf("Enter the number of elements: ");
    scanf("%d", &size);

    int Array[size];
    printf("Enter %d elements: ", size);
    for(int i = 0; i < size; i++){
        scanf("%d", &Array[i]);
    }

    printf("\nArray before sorting: \n");
    printArray(Array, size);

    mergeSort(Array, size);

    printf("\nArray after sorting: \n");
    printArray(Array, size);

    return 0;
}
