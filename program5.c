// TO PRINT SECOND HALF OF THE FILE

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

void main() {
    char b[1000];
    int fd = open("v1.txt", O_RDONLY);
    
    int file_size = lseek(fd, 0, SEEK_END);
    int half = file_size / 2;
    
    lseek(fd, half, SEEK_SET);
    
    int n = read(fd, b, 1000);
    write(1, b, n);
    
    close(fd);
}

