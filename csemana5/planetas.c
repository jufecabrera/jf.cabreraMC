#include <stdio.h>
#include <math.h>

double get_x2(double r, double m);
double get_r(double x0,double y0,double z0,double x1,double y1,double z1);
void main(void){
	double h = 0.001;
	int t_max=10000;
	float t[t_max];
	double m0, x0[t_max],y0[t_max],z0[t_max],x01[t_max],y01[t_max],z01[t_max],x02[t_max],y02[t_max],z02[t_max];
	double m1, x1[t_max],y1[t_max],z1[t_max],x11[t_max],y11[t_max],z11[t_max],x12[t_max],y12[t_max],z12[t_max];
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

	double ri=get_r(x0[0],y0[0],z0[0],x1[0],y1[0],z1[0]);	

	x02[0] = -(x0[0]-x1[0])*get_x2(ri,m1)/ri;
	y02[0] = -(y0[0]-y1[0])*get_x2(ri,m1)/ri;
	z02[0] = -(z0[0]-z1[0])*get_x2(ri,m1)/ri;
	
	x12[0] = -(x1[0]-x0[0])*get_x2(ri,m0)/ri;
	y12[0] = -(y1[0]-y0[0])*get_x2(ri,m0)/ri;
	z12[0] = -(z1[0]-z0[0])*get_x2(ri,m0)/ri;

	x01[1] = x01[0]+x02[0]*h;
	y01[1] = y01[0]+y02[0]*h;
	z01[1] = z01[0]+z02[0]*h;

	x11[1] = x11[0]+x12[0]*h;
	y11[1] = y11[0]+y12[0]*h;
	z11[1] = z11[0]+z12[0]*h;

	for(i=2;i<t_max;i++){
		t[i]=t[i-1]+h;
		double r=get_r(x0[i-1],y0[i-1],z0[i-1],x1[i-1],y1[i-1],z1[i-1]);
		x02[i-1] = -(x0[i-1]-x1[i-1])*get_x2(r,m1)/r;
		y02[i-1] = -(y0[i-1]-y1[i-1])*get_x2(r,m1)/r;
		z02[i-1] = -(z0[i-1]-z1[i-1])*get_x2(r,m1)/r; 	
		x12[i-1] = -(x1[i-1]-x0[i-1])*get_x2(r,m0)/r;
		y12[i-1] = -(y1[i-1]-y0[i-1])*get_x2(r,m0)/r;
		z12[i-1] = -(z1[i-1]-z0[i-1])*get_x2(r,m0)/r;
		x0[i] = x0[i-2]+x01[i-1]*h*2;
		y0[i] = y0[i-2]+y01[i-1]*h*2;
		z0[i] = z0[i-2]+z01[i-1]*h*2;
		x1[i] = x1[i-2]+x11[i-1]*h*2;
		y1[i] = y1[i-2]+y11[i-1]*h*2;
		z1[i] = z1[i-2]+z11[i-1]*h*2; 
		x01[i] = x01[i-2]+x02[i-1]*h*2;
		y01[i] = y01[i-2]+y02[i-1]*h*2;
		z01[i] = z01[i-2]+z02[i-1]*h*2;
		x11[i] = x11[i-2]+x12[i-1]*h*2;
		y11[i] = y11[i-2]+y12[i-1]*h*2;
		z11[i] = z11[i-2]+z12[i-1]*h*2;
	}
	for(i=0;i<t_max;i++){
		printf("%f,%e,%e,%e,%e,%e,%e\n",t[i],x0[i],y0[i],z0[i],x1[i],y1[i],z1[i]);	
	}
}
double get_x2(double r, double m){
	double G = 1.985229E-29;
	double a;
	a = G*m/(r*r);
	return a;
}
double get_r(double x0,double y0,double z0,double x1,double y1,double z1){
	double r;
	r=sqrt((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)+(z0-z1)*(z0-z1));
	return r;
}

