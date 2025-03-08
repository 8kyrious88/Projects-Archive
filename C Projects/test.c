#include <stdio.h>
int main() {
    FILE *filePointer;
    int numbers[5];
    // Open the file in binary read mode
    filePointer = fopen("numbers.bin", "rb");
    if (filePointer == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }
    // Move the file pointer to the second integer (index 1)
    // Read the integer at the current position
    fread(&numbers, sizeof(int), 5, filePointer);
    for (int i =0; i<5; i++) {
        printf("Num: %d\n", numbers[i]);
    }
    // Close the file
    fclose(filePointer);
    return 0;
}