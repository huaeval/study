// #include <stdio.h>
 
// int max(int x, int y)
// {
//     return x > y ? x : y;
// }
 
// int main(void)
// {
//     /* p 是函数指针 */
//     int (* p)(int, int) = & max; // &可以省略
//     int a, b, c, d;
//     // printf(p);
//     printf("请输入三个数字:");
//     scanf("%d %d %d", & a, & b, & c);
 
//     /* 与直接调用函数等价，d = max(max(a, b), c) */
//     d = p(p(a, b), c); 
 
//     printf("最大的数字是: %d\n", d);
 
//     return 0;
// }

#include <stdio.h>
 
int main ()
{
   int  var1;
   char var2[10];
   printf("var1 变量的地址： %p\n", &var1  );
   printf("var2 变量的地址： %p\n", &var2  );
 
   return 0;
}