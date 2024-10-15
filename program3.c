// TO COPY ENTIRE CONTENT FROM ONE FILE AND WRITE INTO ANOTHER FILE (HERE CONTENT IS MORE THAN 100 CHARACTERS)

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

void main() {
    char b[1000];
    int fd = open("v1.txt", O_RDONLY);
    int fd1 = open("v2.txt", O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    int n = read(fd, b, 1000);
    write(fd1, b, n);
    close(fd);
    close(fd1);
}
