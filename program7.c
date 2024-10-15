//  TO PRINT THE FIRST 15 CHARACTERS FROM THE FILE

#include <stdio.h>
#include <fcntl.h>   // For open()
#include <unistd.h>  // For read(), close()

int main() {
    int fd;
    char buffer[16];  // Buffer to hold 15 characters + 1 for null terminator
    ssize_t bytesRead;

    // Open the file in read-only mode
    fd = open("your_file.txt", O_RDONLY);
    
    if (fd == -1) {
        perror("Error opening the file");
        return 1;
    }

    // Read up to 15 characters from the file
    bytesRead = read(fd, buffer, 15);

    if (bytesRead == -1) {
        perror("Error reading the file");
        close(fd);
        return 1;
    }

    // Null-terminate the buffer to make it a proper string
    buffer[bytesRead] = '\0';

    // Print the first 15 characters
    printf("First 15 characters: %s\n", buffer);

    // Close the file
    close(fd);

    return 0;
}
