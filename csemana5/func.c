#include <stdio.h>
#define PI 3.14159

void print_points(int n_points);
float get_surface(float radius);
float get_volume(float radius);

int main(void){
	int n_points = 20;
	print_points(n_points);
	return 0;
}
void print_points(int n_points){
	int i;
	float radius = 0.0;
	float volume = 0.0;
	float surface = 0.0;
	printf("Radius Surface Volume\n");
	for(i=0;i<n_points;i++){
		radius = 1.0*i;
		surface = get_surface(radius);
		volume = get_volume(radius); 
		printf("%f %f %f\n", radius, surface, volume);
	}
}
float get_surface(float radius){
	float sur;
	sur = 4.0 * PI * radius * radius;
	return sur;
}
float get_volume(float radius){
	float vol;
	vol = (4.0/3.0)*PI*radius*radius*radius;
	return vol;
}

