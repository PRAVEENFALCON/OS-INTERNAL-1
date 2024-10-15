#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) { // Error in creating a child
        printf("Child cannot be created\n");
    } 
    else if (pid > 0) { // Parent section
        printf("Process id of child = %d\n", pid);
        printf("Process id of parent = %d\n", getpid());

        int status;
        pid_t child_pid = wait(&status); // Parent waits for the child

        if (child_pid > 0) {
            if (WIFEXITED(status)) {
                printf("Child process (PID: %d) exited with status %d\n", child_pid, WEXITSTATUS(status));
            } else {
                printf("Child process (PID: %d) did not terminate normally\n", child_pid);
            }
        } else {
            perror("wait failed");
        }
    } 
    else { // Child section
        sleep(1); // Simulate some work
        printf("Process id of child = %d\n", getpid());
        printf("Process id of parent = %d\n", getppid());
    }

    return 6;
}
