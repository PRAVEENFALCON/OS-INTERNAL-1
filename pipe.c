#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2]; // file descriptors for the pipe
    char buffer[100]; // buffer to store the message

    // Create a pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    // Fork the process
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) { // Child process
        close(fd[1]); // Close write end
        read(fd[0], buffer, sizeof(buffer)); // Read the message from the pipe
        printf("Child received: %s\n", buffer); // Print the message
        close(fd[0]); // Close read end
    } else { // Parent process
        close(fd[0]); // Close read end
        const char *message = "Hello from the parent process!"; // Message to send
        write(fd[1], message, strlen(message) + 1); // Write the message to the pipe
        close(fd[1]); // Close write end
    }

    return 0;
}
