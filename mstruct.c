#include "stdio.h"
#include "string.h"

int main(int argc, char const *argv[])
{
    struct BOOKS
    {
        char name[50];
        char year[12];
    } Book;

    struct BOOKS book1;
    strcpy(book1.year,"2018/12/25");
    strcpy(book1.name,"那个男人那个男人那个男人那个男人1");
    printf("book:%s,%s",book1.name,book1.year);
    return 0;
}

