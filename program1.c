// TO COPY THE CONTENT FROM ONE FILE TO ANOTHER WITHOUT DETETING THE CONTENT OF SECOND FILE

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

void main() {
    char b[100];

    int fd = open("file1.txt", O_RDONLY);
    int fd1 = open("file3.txt", O_WRONLY | O_APPEND);

    int n = read(fd, b, 100);

    write(fd1, b, n);

    close(fd);
    close(fd1);
}
