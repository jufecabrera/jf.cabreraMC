#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int lx = 744;
int ly = 500;
int ind(int y, int x);
void main(void)
{
	int i=0, j=0;
	int *M = malloc((lx*ly)*sizeof(int));
	FILE *file;
	file = fopen("map_data.txt", "r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = " ";
	while(fgets(line_buffer, len, file))
	{
		split_buffer = strtok(line_buffer, delimiter);
		while(split_buffer != NULL)
		{
			M[ind(i,j)] = atoi(split_buffer);
			split_buffer = strtok(NULL, delimiter);
			printf("%d\n",j);
			j += 1;
		}
		j=0;
		i += 1;
	}
	fclose(file);
	for(i=0;i<ly;i++)
	{
		for(j=0;j<lx;j++)
			{
				//printf("%d ",M[ind(i,j)]);
			}
		printf("\n");
	}
}
int ind(int y, int x)
{
	int a = y*lx+x;
	//printf("%d\n",a);
	return a;
}
