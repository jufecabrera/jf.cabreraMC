#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

double h = 0.001;
void step1(double* M, int pla, int dat);
void step(double* M, int pla, int dat , int tie);
double acalc(double* M, int pla, int dat, int tie);
double RT(double* M, int p1, int p2, int tie);
double A(double* M, int p2, double rt);
double v(double* M, double rt, int dat, int p1, int p2, int tie);
int ind(int i, int j, int k);
int main(void){
	int t_max=250000;
	int i=0, j=0, k;
	float t[t_max];
	double *M = malloc((10*8*t_max)*sizeof(double));
	//lectura de los datos
	FILE *file;
	file = fopen("coordinates.csv", "r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = ",";
	while(fgets(line_buffer, len, file)){
		split_buffer = strtok(line_buffer, delimiter);
		while(split_buffer != NULL){
			M[ind(i,j,0)] = atof(split_buffer);
			split_buffer = strtok(NULL, delimiter);
			j += 1;
		}
		j=0;
		i += 1;
	}
/*se calculan los datos en el tiempo 1*/
	t[0] = 0.0;
	t[1]=t[0]+h;
	for(i=0;i<10;i++){ 
		for(j=2;j<8;j++){
			step1(M,i,j);
		}	
	}
/*se calculan los datos para todos los tiempos*/
	for(k=2;k<t_max;k++){
		t[k]=t[k-1]+h;
		for(i=0;i<10;i++){ 
			for(j=2;j<8;j++){
				step(M,i,j,k);
			}	
		}
	}
/*imprimir*/
	for(k=0;k<t_max;k++){
		printf("%f,",t[k]);
		for(j=2;j<5;j++){
			for(i=0;i<10;i++){
				printf("%e",M[ind(i,j,k)]);
				if(i==9 && j==4){
					continue;
				}
				printf(",");			
			}
		}
		printf("\n");			
	}
	return 0;		
}
//calcula los datos en el tiempo 1
void step1(double* M, int pla, int dat){
	if(dat==2||dat==3||dat==4){	
		M[ind(pla,dat,1)]= M[ind(pla,dat,0)]+h*M[ind(pla,(dat+3),0)];
	}
	else{
		M[ind(pla,dat,1)]= M[ind(pla,dat,0)]+h*acalc(M,pla,dat,0);	
	}
}
//calcula los datos para todos los tiempos
void step(double* M, int pla, int dat , int tie){
	if(dat==2||dat==3||dat==4){	
		M[ind(pla,dat,tie)]= M[ind(pla,dat,tie-2)]+2*h*M[ind(pla,dat+3,tie-1)];
	}
	else{
		M[ind(pla,dat,tie)]= M[ind(pla,dat,tie-2)]+2*h*acalc(M,pla,dat,tie-1);	
	}
}
//calcula acelearcion debido a cada planeta
double acalc(double* M, int pla, int dat, int tie){
	int i;	
	double a = 0;	
	for(i=0;i<10;i++){	
		if(i==pla){
			continue;
		}
		double rt = RT(M,pla,i,tie);
		a += A(M,i,rt)*v(M,rt,dat,pla,i,tie);
	}
	return a;
}
//calcula distancia entre dos planetas
double RT(double* M, int p1, int p2, int tie){
	double rt;
	rt = sqrt((M[ind(p1,2,tie)]-M[ind(p2,2,tie)])*(M[ind(p1,2,tie)]-M[ind(p2,2,tie)])+(M[ind(p1,3,tie)]-M[ind(p2,3,tie)])*(M[ind(p1,3,tie)]-M[ind(p2,3,tie)])+(M[ind(p1,4,tie)]-M[ind(p2,4,tie)])*(M[ind(p1,4,tie)]-M[ind(p2,4,tie)]));
	return rt;
}
//calcula acelearcion debido a un planeta
double A(double* M, int p2, double rt){
	double G = 1.985229E-29;
	double a;
	a = G*M[ind(p2,1,0)]/(rt*rt);
	return a;
}
//calculas componenete de aceleracion en un eje
double v(double* M, double rt, int dat, int p1, int p2, int tie){
	double v;
	v = (M[ind(p2,dat-3,tie)]-M[ind(p1,dat-3,tie)])/rt;
	return v;
}
//indice para memoria plana
int ind(int i, int j, int k){
	int a=10*8*k+8*i+j;
	return a;
}






