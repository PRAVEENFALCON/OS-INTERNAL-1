#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    int a = 2;
    pid_t pid;
    pid = fork();

    printf("%d\n", pid);

    if (pid < 0) {
        printf("FORK FAILED\n");
    } else if (pid == 0) {
        printf("CHILD PROCESS \t a is: ");
        printf("%d\n", ++a);
    } else {
        printf("PARENT PROCESS \t a is: ");
        printf("%d\n", --a);
    }

    printf("EXITING WITH X = %d\n", a);
    
    return 0;
}
