#include <stdio.h>
#include <math.h>
#define h 0.01

double get_x2(double r, double m);
double step(double vold, double xoold);
void main(void){
	int t_max=10000;
	float t[];
	double m0, x0[],y0[],z0[],x01[],y01[],z01[],x02[],y02[],z02[];
	double m1, x1[],y1[],z1[],x11[],y11[],z11[],x12[],y12[],z12[];
	int i;
	t[0] = 0.0;
	m0 = 1.99E+30;
	m1 = 5.97E+24;
	x0[0] = 0.0034386459;
	y0[0] = 0.0037956083;
	z0[0] = -0.0001571955;
	x01[0] = -0.0008935944;
	y01[0] = 0.002455013;
	z01[0] = 0.000018102;
	x1[0] = 0.188906033;
	y1[0] = 0.9708143648;
	z1[0] = -0.0001923272;
	x11[0] = -6.2729216283;
	y11[0] = 1.1606780005;
	z11[0] = 0.0001186362;
	for(i=2;i<t_max;i++){
		x[]
		x02[0] = 
	}
}
double get_x2(double r, double m){
	double G = 1.985229E-29;
	double a;
	a = G*m/(r*r);
	return a;
}
double step(double vold, double xoold){	
	double xnew;
	xnew = xoold + 2*h*vold;
	return xnew;
}

