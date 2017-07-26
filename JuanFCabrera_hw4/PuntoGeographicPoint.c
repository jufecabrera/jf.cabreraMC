#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define L 10000

int lx = 744;
int ly = 500;
int ind(int y, int x);
double randnum(void);
void main(void)
{
	int i=0, j=0;
	int *M = malloc((lx*ly)*sizeof(int));
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
	printf("%e\n",randnum());
	return a;
}
double randnum(void)
{
    return (double) rand()/RAND_MAX;
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
			if((xi<0)||(xi>743)||(yi<0)||(yi>499))
			{
				continue;
			}		
			p = M[ind(xi,yi)];
			if(p==0)
			{
				continue;
			}	
			r = pow()
		}
	}
}




