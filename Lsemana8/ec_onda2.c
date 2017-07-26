#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void initial_condition(double *u, int n_x, double delta_x);
void first_iteration(double *u_present, double *u_initial, double n_x, double r);
void update_u(double *u_future, double *u_present, double *u_past, double n_x, double r);
void copy(double *u_new, double *u_old, int n_x);
void print_u(double *u, double n_x, double delta_x);

int main(){
    double x_f = 1.0;
	int n_x = 1000;
	double delta_x = 0.001;

	double delta_t = 5E-4;
	int n_t = 35000.0;
	double c = 1.0;
	double r = c * delta_t/delta_x;
    
    double *u_past = malloc(n_x*sizeof(double));
	double *u_present = malloc(n_x*sizeof(double));
	double *u_future = malloc(n_x*sizeof(double));
    
    initial_condition(u_past, n_x, delta_x);
    u_past[0] = 0.0;
	u_past[n_x-1] = 0.0;
	
	u_present[0] = 0.0;
	u_present[n_x-1] = 0.0;
    
    first_iteration(u_present, u_past, n_x, r);
    int i;
	for(i=0;i<n_t;i++){
		update_u(u_future, u_present, u_past, n_x, r);
		copy(u_present, u_past, n_x);
		copy(u_future, u_present, n_x);
	}
	print_u(u_present, n_x, delta_x);

    return 0;
}
void initial_condition(double *u, int n_x, double delta_x){
	
	int i;
	for(i=0;i<n_x;i++){
		double x = i*delta_x;
		u[i] = exp(-pow((x-0.3),2.0)/0.01);
	}
}
void first_iteration(double *u_present, double *u_initial, double n_x, double r){
	int i;
	for(i=1;i<n_x-1;i++){
		u_present[i] = u_initial[i] + pow(r, 2.0)/2.0 * (u_initial[i+1] - 2.0*u_initial[i] + u_initial[i-1]);
	}
}
void update_u(double *u_future, double *u_present, double *u_past, double n_x, double r){
	int i;
	for(i=1;i<n_x-1;i++){
		u_future[i] = (2.0*(1.0-pow(r,2.0)))*u_present[i] - u_past[i] + (pow(r,2.0))*(u_present[i+1] +  u_present[i-1]);
	}
}
void copy(double *u_new, double *u_old, int n_x){
	int i;
	for(i=0;i<n_x;i++){
		u_old[i] = u_new[i];
	}
}
void print_u(double *u, double n_x, double delta_x){
	int i;
	for(i=0;i<n_x;i++){
		printf("%f %f\n", i*delta_x ,u[i]);
	}
}





