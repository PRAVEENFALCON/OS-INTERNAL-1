// TO READ FROM ONE FILE AND WRITE INTO ANOTHER FILE

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

void main() {
    char b[100];
    int fd = open("file1.txt", O_RDONLY);
    int fd1 = open("files.txt", O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    int n = read(fd, b, 100);
    write(fd1, b, n);
    close(fd);
    close(fd1);
}
