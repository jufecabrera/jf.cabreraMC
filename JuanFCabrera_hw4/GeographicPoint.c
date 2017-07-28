#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define iter 5000

int lx = 744;
int ly = 500;
int indl(int i, int d);
int ind(int y, int x);
double randnum(void);
void first(double* L, int* M);
void algor(double* L,int* M);
double get_r(int* M,int x, int y);
int rmax(double* L);
void imprim(double* L);
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
	srand((unsigned)time(NULL));
	first(L,M);
	algor(L,M);	
	imprim(L);
}
int ind(int y, int x)
{
	int a = y*lx+x;
	return a;
}
int indl(int i, int d)
{
	int a = i*3+d;
	return a;
}
double randnum(void)
{
	double ran = ((double) rand()/RAND_MAX);
	return ran;
}
void first(double* L, int* M)
{
	int agua = 1;
	int x;
	int y;
	while(agua)
	{
		x = randnum()*lx;
		y = randnum()*ly;
		if(M[ind(y,x)]==0)
		{
			agua = 0;
		}
	}
	L[indl(0,0)]=x;
	L[indl(0,1)]=y;
	L[indl(0,2)]=get_r(M,x,y);
}
void algor(double* L,int* M)
{
	int xa;
	int ya;
	int i;
	int agua;
	double r;
	double alpha, beta;
	for(i=1;i<iter;i++)
	{
		agua =1;
		while(agua)
		{
			xa = 300*(2*randnum()-1)+L[indl(i-1,0)];
			ya = 300*(2*randnum()-1)+L[indl(i-1,1)];
			xa = xa%lx;
			ya = ya%ly;			
			if(xa<0)
			{
				xa = lx+xa;
			}
			if(ya<0)
			{
				ya = ly+ya;
			}
			if(M[ind(ya,xa)]==0)
			{
				agua = 0;
			}
		}
		r = get_r(M,xa,ya);
		alpha = exp((r-L[indl(i-1,2)])*10);
		if(alpha > 1)
		{
			L[indl(i,0)]=xa;
			L[indl(i,1)]=ya;
			L[indl(i,2)]=r;
		}
		else
		{
			beta = randnum();
			if(alpha>beta)
			{
				L[indl(i,0)]=xa;
				L[indl(i,1)]=ya;
				L[indl(i,2)]=r;
			}
			else
			{
				L[indl(i,0)]=L[indl(i-1,0)];
				L[indl(i,1)]=L[indl(i-1,1)];
				L[indl(i,2)]=L[indl(i-1,2)];
			}
		}
	}
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
	for(i=0;i<200;i++)
	{
		for(j=0;j<200;j++)
		{
			xi = x-100+j;
			yi = y-100+i;
			xi = xi%lx;
			yi = yi%ly;
			if(xi<0)
			{
				xi = lx+xi;
			}
			if(yi<0)
			{
				yi = ly+yi;
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
int rmax(double* L)
{
	double max=0;
	int imax;
	int i;
	for(i=0;i<iter;i++)
	{
		if(L[indl(i,2)]>max)
		{
			max=L[indl(i,2)];
			imax=i;
		}
	}
	return imax;
}
void imprim(double* L)
{
	int i = rmax(L);
	double x = L[indl(i,0)]*(360.0/744.0)-180;
	double y = L[indl(i,1)]*(-180.0/500.0)+90;
	double r = L[indl(i,2)];	
	printf("Las coordenadas del punto mas alejado son: longitud:%f, latitud:%f\n",(float)x,(float)y);
	FILE *f = fopen("m.txt","w");
	fprintf(f, "%e %e %e\n",x,y,r);
	fclose(f);
}


