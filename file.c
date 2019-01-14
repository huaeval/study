#include <stdio.h>
void creted();
void read();
int main()
{
//    creted();
   read();
}

void creted(){
   FILE *fp = NULL;
   fp = fopen("./tmp/test.txt", "w+");
   fprintf(fp, "This is testing for fprintf...\n");
   fputs("This is testing for fputs...\n", fp);
   fclose(fp);
}

void read(){
    FILE *fp = NULL;
    char buff[255];
    fp = fopen("./tmp/test.txt", "r");
    fscanf(fp, "%s", buff);
    printf("1: %s\n", buff );
    
    fgets(buff, 255, (FILE*)fp);
    printf("2: %s\n", buff );
    
    fgets(buff, 255, (FILE*)fp);
    printf("3: %s\n", buff );
    fclose(fp);
}