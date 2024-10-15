#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int pid = fork();

    if (pid < 0) {
        printf("Fork failed\n");
        return 1;
    } 
    else if (pid == 0) {
        execl("/bin/ls", "ls", NULL);
        perror("execl failed");
        exit(1);
    } 
    else {
        wait(NULL);
        printf("Child process complete\n");
    }

    return 0;
}

