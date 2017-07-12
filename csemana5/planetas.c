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
	t[1]=t[0]+h;
	m0 = 1.99E+30;
	m1 = 5.97E+24;

	x0[0] = 0.0034386459;
	y0[0] = 0.0037956083;
	z0[0] = -0.0001571955;

	x01[0] = -0.0008935944;
	y01[0] = 0.002455013;
	z01[0] = 0.000018102;

	x0[1] = x0[0]+x01[0]*h;
	y0[1] = y0[0]+y01[0]*h;
	z0[1] = z0[0]+z01[0]*h;

	x1[0] = 0.188906033;
	y1[0] = 0.9708143648;
	z1[0] = -0.0001923272;

	x11[0] = -6.2729216283;
	y11[0] = 1.1606780005;
	z11[0] = 0.0001186362;

	x1[1] = x1[0]+x11[0]*h;
	y1[1] = y1[0]+y11[0]*h;
	z1[1] = z1[0]+z11[0]*h;

	x02[0] = get-x2(x0[0]-x1[0],m1);
	y02[0] = get-x2(y0[0]-y1[0],m1);
	z02[0] = get-x2(z0[0]-z1[0],m1);
	
	x12[0] = get-x2(x1[0]-x0[0],m0);
	y12[0] = get-x2(y1[0]-y0[0],m0);
	z12[0] = get-x2(z1[0]-z0[0],m0);

	x01[1] = x01[0]+x02[0]*h;
	y01[1] = y01[0]+y02[0]*h;
	z01[1] = z01[0]+z02[0]*h;

	x11[1] = x11[0]+x12[0]*h;
	y11[1] = y11[0]+y12[0]*h;
	z11[1] = z11[0]+z12[0]*h;

	for(i=2;i<t_max;i++){
		t[i]=t[i-1]+h;
		x02[i-1] = get-x2(x0[i-1]-x1[i-1],m1);
		y02[i-1] = get-x2(y0[i-1]-y1[i-1],m1);
		z02[i-1] = get-x2(z0[i-1]-z1[i-1],m1); 	
		x12[i-1] = get-x2(x1[i-1]-x0[i-1],m0);
		y12[i-1] = get-x2(y1[i-1]-y0[i-1],m0);
		z12[i-1] = get-x2(z1[i-1]-z0[i-1],m0);
		x0[i] = x0[i-2]+x01[i-1]*h*2;
		y0[i] = y0[i-2]+y01[i-1]*h*2;
		z0[i] = z0[i-2]+z01[i-1]*h*2; 
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

