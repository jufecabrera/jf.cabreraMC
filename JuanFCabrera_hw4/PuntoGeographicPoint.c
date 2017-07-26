#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define iter 10000

int lx = 744;
int ly = 500;
int ind(int y, int x);
double randnum(void);
double get_r(int* M,int x, int y);
void imprim(int* M);
void main(void)
{
	int i=0, j=0;
	int *M = malloc((lx*ly)*sizeof(int));
	double *L = malloc((iter*3)*sizeof(double));
	FILE *file;
	file = fopen("map_data.txt", "r");
	int len = 2000;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = " ";
	while(fgets(line_buffer, len, file))
	{
		split_buffer = strtok(line_buffer, delimiter);
		while(split_buffer != NULL)
		{
			M[ind(i,j)] = atoi(split_buffer);
			split_buffer = strtok(NULL, delimiter);
			j += 1;
		}
		j=0;
		i += 1;
	}
	fclose(file);
}
int ind(int y, int x)
{
	int a = y*lx+x;
	return a;
}
double randnum(void)
{
	double ran =    2*((double) rand()/RAND_MAX)-1;
	return ran;
}
void first(double* L, int* M)
{
	int agua = 1;
	while(agua)
	{
		
	}
}
void algor(int* M)
{
	int xa;
	int ya;
	
}
double get_r(int* M,int x, int y)
{
	int i;
	int j;
	double min;
	double r;
	int xi;
	int yi;
	int p;
	min = 1000.0;
	for(i=0;i<300;i++)
	{
		for(j=0;j<300;j++)
		{
			xi = x-150+j;
			yi = y-150+i;
			xi = xi%lx;
			yi = yi%ly;
			if(xi<0)
			{
				xi = xl+xi;
			}
			if(yi<0)
			{
				yi = yl+yi;
			}		
			p = M[ind(yi,xi)];
			if(p==0)
			{
				continue;
			}	
			r = sqrt(pow(xi-x,2)+pow(yi-y,2));
			if(r<min)
			{
				min = r;
			}		
		}
	}
	return min;
}
void imprim(int* M)
{
	int i,j;
	FILE *f = fopen("m.txt","w");
	for(j=0;j<ly;j++)
	{
		for(i=0;i<lx;i++)
		{
			fprintf(f, "%d ",M[ind(j,i)]);
		}
		fprintf(f, "\n");
	}
	fclose(f);
}


