// TO PRINT CHARACTERS FROM 10TH TO 20TH POSITION OF A FILE

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

void main() {
    char b[11];
    int fd = open("v1.txt", O_RDONLY);
    
    lseek(fd, 9, SEEK_SET);
    
    int n = read(fd, b, 10);
    write(1, b, n);
    
    close(fd);
}
