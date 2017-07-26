#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double func(double t,float N0,float gamma);
void fill_t(double t,float N0);
void calc_y(double *y,float N0,float gamma);
void estoc(float N0, float* n, float gamma);
void estocp(float N0, float* np, float gamma);
void imprim(double *y,float* n, float*np);
void main(void)
{
	int i;
	int it=1000;
	float N0= 10.0;
	double gamma = 0.5;
	double *y = malloc(1000*sizeof(double));
	float *n = malloc(1000*sizeof(float));
	float *np = malloc(1000*sizeof(float));
	calc_y(y,N0,gamma);
	srand48(1);
	estoc(N0, n, gamma);	
	for(i=0; i<1000;i++)
	{
		np[i]=0;
	}
	for(i=0; i<it;i++)
	{
		estocp(N0,np,gamma);
	}
	for(i=0; i<1000;i++)
	{
		np[i]=np[i]/it;
	}
	imprim(y,n,np);
}

double func(double t,float N0,float gamma)
{
	return N0*exp(-gamma*t);
}
void calc_y(double *y,float N0,float gamma)
{
	int i;
	for(i=0;i<1000;i++)
	{
		y[i]=func(i*(1.0/100.0),N0,gamma);
	}
}
void estoc(float N0, float* n, float gamma)
{
	n[0]= N0;
	float p;
	int i;
	float dt = 0.01;
	for(i=1; i<1000;i++)
	{
		p = gamma*N0*dt;		
		if(drand48()<p)
		{
			N0=N0-1;			
		}
		n[i]=N0;
	}
}
void estocp(float N0, float* np, float gamma)
{
	int i;
	float p;
	float dt = 0.01;
	for(i=0; i<1000;i++)
	{
		p = gamma*N0*dt;		
		if(drand48()<p)
		{
			N0=N0-1;			
		}
		np[i]= np[i]+N0;
	}
}
void imprim(double *y,float* n, float* np)
{
	int i;
	for(i=0;i<1000;i++)
	{	
		printf("%e %e %e\n",y[i],n[i],np[i]);
	}
}
