#include <stdio.h>
#include <math.h>
main(void){
	int lista[10];
	int i;
	printf("Content before initialization\n");
	for(i=0;i<10;i++){
		printf("%d\n", lista[i]);	
	}
	for(i=0;i<10;i++){
		lista[i] = i*2;	
	}
	printf("Content after initialization\n");
	for(i=0;i<10;i++){
	printf("%d\n", lista[i]);
	}
}

