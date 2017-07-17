#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int t_max=10000;
double h = 0.001;
void step1(double M[10][8][t_max], int pla, int dat);
void step(double M[10][8][t_max], int pla, int dat , int tie);
double acalc(double M[10][8][t_max], int pla, int dat, int tie);
double RT(double M[10][8][t_max], int p1, int p2, int tie);
double A(double M[10][8][t_max], int p2, double rt);
double v(double M[10][8][t_max], double rt, int dat, int p1, int p2, int tie);
int main(void){
	float t[t_max];
	double M[10][8][t_max];
	FILE *file;
	file = fopen("coordinates.csv", "r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = ",";
	int i=0, j=0, k;
	while(fgets(line_buffer, len, file)){
		split_buffer = strtok(line_buffer, delimiter);
		while(split_buffer != NULL){
			M[i][j][0] = atof(split_buffer);
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
		for(j=2;j<8;j++){
			for(i=0;i<10;i++){
				printf("%e",M[i][j][k]);
				if(i==9 && j==7){
					continue;
				}
				printf(",");			
			}
		}
		printf("\n");			
	}
	return 0;		
}
void step1(double M[10][8][t_max], int pla, int dat){
	if(dat==2||dat==3||dat==4){	
		M[pla][dat][1]= M[pla][dat][0]+h*M[pla][dat+3][0];
	}
	else{
		M[pla][dat][1]= M[pla][dat][0]+h*acalc(M,pla,dat,0);	
	}
}
void step(double M[10][8][t_max], int pla, int dat , int tie){
	if(dat==2||dat==3||dat==4){	
		M[pla][dat][tie]= M[pla][dat][tie-2]+2*h*M[pla][dat+3][tie-1];
	}
	else{
		M[pla][dat][tie]= M[pla][dat][tie-2]+2*h*acalc(M,pla,dat,tie-1);	
	}
}
double acalc(double M[10][8][t_max], int pla, int dat, int tie){
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
double RT(double M[10][8][t_max], int p1, int p2, int tie){
	double rt;
	rt = sqrt((M[p1][2][tie]-M[p2][2][tie])*(M[p1][2][tie]-M[p2][2][tie])+(M[p1][3][tie]-M[p2][3][tie])*(M[p1][3][tie]-M[p2][3][tie])+(M[p1][4][tie]-M[p2][4][tie])*(M[p1][4][tie]-M[p2][4][tie]));
	return rt;
}
double A(double M[10][8][t_max], int p2, double rt){
	double G = 1.985229E-29;
	double a;
	a = G*M[p2][1][0]/(rt*rt);
	return a;
}
double v(double M[10][8][t_max], double rt, int dat, int p1, int p2, int tie){
	double v;
	v = (M[p2][dat-3][tie]-M[p1][dat-3][tie])/rt;
	return v;
}







