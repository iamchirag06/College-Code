#include <stdio.h>

#define MAX_FRAMES 10
#define MAX_PAGES 100

void fifo_page_replacement(int pages[], int n, int frames)
{
    int frame[MAX_FRAMES], front = 0, count = 0, page_faults = 0;
    
    for (int i = 0; i < frames; i++)
        frame[i] = -1; // Initialize frames with -1 (empty)

    printf("Page Reference String: ");
    for (int i = 0; i < n; i++)
        printf("%d ", pages[i]);
    printf("\n\n");

    printf("Frame Status after each page reference:\n");
    for (int i = 0; i < n; i++) {
        int found = 0;

        // Check if page is already in frame
        for (int j = 0; j < frames; j++) {
            if (frame[j] == pages[i]) {
                found = 1;
                break;
            }
        }

        // If page fault occurs
        if (!found) {
            frame[front] = pages[i];
            front = (front + 1) % frames; // FIFO queue behavior
            page_faults++;
        }

        // Print current frame status
        for (int j = 0; j < frames; j++) {
            if (frame[j] != -1)
                printf("%d ", frame[j]);
            else
                printf("- ");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults: %d\n", page_faults);
}

int main()
{
    int pages[MAX_PAGES], n, frames;
    
    printf("Enter the number of pages: ");
    scanf("%d", &n);
    
    printf("Enter the page reference string: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &pages[i]);
    
    printf("Enter the number of frames: ");
    scanf("%d", &frames);
    
    fifo_page_replacement(pages, n, frames);
    
    return 0;
}