#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double func(double x);
void imprim(double r);
void main(void)
{
	int points = 100000;
	int c = 0;
	int i;
	double x;
	double y;
	srand48((unsigned)time(NULL));
	for(i=0; i<points; i++)
	{
		x = drand48();
		y = drand48();
		if(y<=func(x))
		{
			c = c+1;
		}
	}
	double r = (double)c/(double)points;
	imprim(r);
}

double func(double x)
{
	double r = exp(-x);	
	return r;
}
void imprim(double r)
{
	FILE *f = fopen("resultados.txt","a");
	fprintf(f, "El valor de la integral es: %f\n",(float)r);
	fclose(f);
}
