#include <stdio.h>
#include <math.h>
main(void){
printf("Hello World\n");
int a =1;
int b =10;
int c= pow(a,b);
float d=1.0;
float e=10.0;
float f= pow(d,e);
printf("%d %d %d \n",a,b,c);
printf("%f %f %f \n",d,e,f);
char s[20] = "La respuesta es: ";
int i = 42;
float x = 42.0;
double y = 42.0;
printf("%s %d %f %e\n", s,i,x,y);
printf("%s %d %d %d\n", s,i,x,y);
}
