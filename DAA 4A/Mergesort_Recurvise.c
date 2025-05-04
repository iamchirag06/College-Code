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

// MergeSort
void mergeSort(int Arr[], int l, int r){
    if(l < r){
        int mid = (l + r) / 2;
        mergeSort(Arr, l, mid);
        mergeSort(Arr, mid + 1, r);
        merge(Arr, l, mid, r);
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

    mergeSort(Array, 0, size - 1);

    printf("\nArray after sorting: \n");
    printArray(Array, size);

    return 0;
}
