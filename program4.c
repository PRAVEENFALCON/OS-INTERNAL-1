// TO PRINT LAST 10 CHARACTERS OF A FILE ONTO THE TERMINAL SCREEN

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

void main() {
    char b[200];
    int fd = open("file3.txt", O_RDWR);
    
    lseek(fd, -11, SEEK_END);
    int n = read(fd, b, 11);
    write(1, b, n);
    
    close(fd);
}
