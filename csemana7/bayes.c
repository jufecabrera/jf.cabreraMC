#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

double likehood(double M[40][2],double Mm[40]);
double[40] mM(double M[40][2], double m, double b);
int main(void){
	int n_iter=20000;
	int i=0, j=0;
	double M[40][2];
	FILE *file;
	file = fopen("obs_data.dat", "r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = " ";
	while(fgets(line_buffer, len, file)){
		split_buffer = strtok(line_buffer, delimiter);
		while(split_buffer != NULL){
			M[i][j] = atof(split_buffer);
			split_buffer = strtok(NULL, delimiter);
			j += 1;
		}
		j=0;
		i += 1;
	}
	
return 0;
}
double likehood(double M[40][2],double Mm[40]){
	double sum =0;
	int i;
	for(i=0;i<40;i++){
		sum += (M[i][1]-Mm[i])*(M[i][1]-Mm[i]);
	}
	double chi = (1.0/2.0)*sum;
	return exp(-chi);
}
double[40] mM(double M[40][2], double m, double b){
	int i;
	double mod[40];
	for(i=0;i<40;i++){
		mod[i]=M[i][0]*m+b;
	}
	return mod;
}

