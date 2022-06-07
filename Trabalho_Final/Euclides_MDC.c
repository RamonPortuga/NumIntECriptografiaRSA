#include <stdio.h>
void euclides (int a, int b, int c);
int main(void){
	int a = 1, b = 1, c = 1;
	while(a > 0){
		scanf ("%d%d", &a, &b);
		euclides (a, b, 1);
	}
}
void euclides (int a, int b, int c){
	c = a / b;
	printf ("\n%d\t%d\t\t%d", a, b, c);
	int resto = a % b;
	if (resto == 0){
		printf ("\nMDC %c igual a : %d\n\n", 130, b);
	}
	else{
		euclides (b, resto, c);
	}
}
