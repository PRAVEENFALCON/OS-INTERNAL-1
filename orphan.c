#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {  // Error in creating a child
        printf("Child cannot be created\n");
    } 
    else if (pid > 0) {  // Parent section
        printf("Process id of child = %d\n", pid);
        printf("Process id of parent = %d\n", getpid());
    } 
    else {  // Child section
        sleep(1);  // Simulate delay to show the child becoming an orphan
        printf("Process id of child = %d\n", getpid());
        printf("Process id of parent = %d\n", getppid());  // Shows parent's process ID
    }

    return 0;
}
