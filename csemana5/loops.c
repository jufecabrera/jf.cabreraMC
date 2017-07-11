#include <stdio.h>
#include <math.h>
#define PI 3.14159
main(void){
	int i;
	float radius=0.0;
	float volume=0.0;
	float surface=0.0;

	printf("Radius Surface Volume\n");
	for(i=0; i<12; i++){
	radius = i;
	surface = 4.0 * PI * radius * radius;
	volume = (4.0/3.0) * PI * radius * radius * radius;
	printf("%f %f %f\n", radius, surface, volume);
	}
}
