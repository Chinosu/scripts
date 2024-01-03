#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char** argv)
{
    if (argc < 2)
    {
        printf("not enough arguments\n");
        exit(EXIT_FAILURE);
    }
    if (argc > 2)
    {
        printf("too many arguments\n");
        exit(EXIT_FAILURE);
    }

    int x = atoi(argv[1]);
    printf("%d\n", x * x);
}
