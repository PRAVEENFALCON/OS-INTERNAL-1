#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {  // Error in creating a child
        printf("Child cannot be created\n");
    } 
    else if (pid > 0) {  // Parent section
        sleep(1);  // Sleep to ensure child doesn't become orphan
        printf("Process id of child = %d\n", pid);  // pid holds child's PID
        printf("Process id of parent = %d\n", getpid());
    } 
    else {  // Child section
        printf("Process id of child = %d\n", getpid());
        printf("Process id of parent = %d\n", getppid());
    }

    return 0;
}
