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
        printf("CHILD PROCESS \t a is: %d\n", ++a);
        printf("I AM THE CHILD AND MY PROCESS ID IS %d\n", getpid());
        printf("I AM THE CHILD AND MY PARENT'S PROCESS ID IS %d\n", getppid());
    } else {
        printf("PARENT PROCESS \t a is: %d\n", --a);
        printf("I AM THE PARENT AND MY PROCESS ID IS %d\n", getpid());
        printf("I AM THE PARENT AND MY CHILD'S PROCESS ID IS %d\n", pid);
    }
    
    printf("EXITING WITH X = %d\n", a);
    
    return 0;
}
