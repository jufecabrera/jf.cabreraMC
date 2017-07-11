#include <stdio.h>
#include <math.h>
#include <stdlib.h>
main(void){
	int a = 429899999;
	int i;
	for(i=0;i<10000000000;i++){
		a = a+1;
		if(a<0){
			printf("%d\n", a-1);
 			break;
		}
			
	}
	/*future arrays*/
	int *array_int;
	/*number of points in the array*/
	int n_points;
	n_points =10;
	/*data allocation*/
	array_int = malloc(n_points*sizeof(int));
	/*check if everything went OK*/	
	if(!array_int){
		printf("There is something wrong with array int\n");
		exit(1);
	} 
	/*print the memory address*/
	printf("Memory starts at %p\n", array_int);
	/*fill the array with data*/
	printf("Allocation went OK. Initializing...\n");
	for(i=0;i<n_points;i++){
		array_int[i] = i*2;
		printf("%d\n", array_int[i]);	
	}
	printf("Let´s see what happens if I go a bit beyond the allocated space...\n");
	array_int[n_points] = n_points * 2;
	printf("%d\n", array_int[n_points]);
	printf("OK.");
	printf("and if I go far away?\n");
	array_int[n_points * 10000] = n_points * 10000 * 2;
	printf("%d\n", array_int[n_points * 10000]);
	printf("everything went just fine\n");
}
