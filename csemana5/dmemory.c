#include <stdio.h>
#include <math.h>
#include <stdlib.h>
void main(void){
	int i;
	int *array_int;
	int n_points = 10;
	array_int = malloc(n_points*sizeof(int));
	if(!array_int){
		printf("There is something wrong with array int\n");
		exit(1);
	} 
	/*memory address*/
	printf("Memory starts at %p\n", array_int);
	/*fil the array*/
	printf("Alocation went OK. Initializing...\n");
	for(i=0;i<n_points;i++){
		array_int[i] = i*2;
		printf("%d\n", array_int[i]);
	}
	printf("Let´s see what happens if we go a bit beyond the allocated space...\n");
	array_int[n_points] = n_points*2;
	printf("%d\n", array_int[n_points]);
	printf("OK.\n");
	/*far away*/
	printf("and if we go far away?\n");
	array_int[n_points*10000] = n_points *10000 *2;
	printf("%d\n", array_int[n_points * 10000]);
	printf("everything went just fine\n");
}
