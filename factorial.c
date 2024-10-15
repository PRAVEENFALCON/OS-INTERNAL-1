#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int n;
    pid_t pid;

    printf("Enter an integer: ");
    scanf("%d", &n);

    pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } 
    else if (pid == 0) {
        unsigned long long result = factorial(n);
        printf("The factorial of %d is: %llu\n", n, result);
    } 
    else {
        wait(NULL);
    }

    return 0;
}


