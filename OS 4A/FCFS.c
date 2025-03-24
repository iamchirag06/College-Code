#include <stdio.h>

int main() {
    int n, bt[30], wait_t[30], turn_ar_t[30], av_wait_t = 0, av_turn_ar_t = 0, i, j;
    
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    
    printf("Enter burst time for each process:\n");
    for (i = 0; i < n; i++) {
        printf("P[%d]: ", i + 1);
        scanf("%d", &bt[i]);
    }

    wait_t[0] = 0; // Waiting time for the first process is 0

    // Calculating waiting time
    for (i = 1; i < n; i++) {
        wait_t[i] = 0;
        for (j = 0; j < i; j++)
            wait_t[i] += bt[j];
    }

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");

    // Calculating turnaround time and displaying process info
    for (i = 0; i < n; i++) {
        turn_ar_t[i] = bt[i] + wait_t[i];
        av_wait_t += wait_t[i];
        av_turn_ar_t += turn_ar_t[i];
        
        printf("P[%d]\t%d\t\t%d\t\t%d\n", i + 1, bt[i], wait_t[i], turn_ar_t[i]);
    }

    av_wait_t /= n;
    av_turn_ar_t /= n;

    printf("\nAverage Waiting Time: %d", av_wait_t);
    printf("\nAverage Turnaround Time: %d\n", av_turn_ar_t);

    return 0;
}
