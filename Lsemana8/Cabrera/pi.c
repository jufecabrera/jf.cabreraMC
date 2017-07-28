#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double func(double x,double y);
void imprim(double r);
void main(void)
{
	int points = 20000000;
	int c = 0;
	int i;
	double x;
	double y;
	double r;
	srand48(1);
	for(i=0;i<points;i++)
	{
		x = drand48();
		y = drand48();
		if(func(x,y)<=1)
		{
			c = c+1;
		}
	}
	r = 4*(double)c/(double)points;
	imprim(r);	
}

double func(double x,double y)
{
	double r = sqrt(x*x+y*y);	
	return r;
}
void imprim(double r)
{
	FILE *f = fopen("resultados.txt","a");
	fprintf( f,"El valor de la constante pi es: %f\n",(float)r);
	fclose(f);
}
