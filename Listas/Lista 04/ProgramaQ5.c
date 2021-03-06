#include <stdio.h>
void num_k_divisoes (int k);
void euclides (int dividendo, int divisor, int resto);
/*Aqui, o main tem como objetivo pedir ao usu?rio o n?mero k
de divis?es e chamar a primeira fun??o para dar prosseguimento 
ao programa */
int main(void){
	int k;
	printf ("Entre com o valor k:\t");
	scanf ("%d", &k);
	num_k_divisoes (k);
}
/*Essa fun??o tem como objetivo calcular dois exemplares de
numeros (no caso, "a" e "b") onde o calculo de seu mdc realiza
exatamente k divis?es.*/
void num_k_divisoes (int k){
	int a = 2, b = 1, cont = 1, c;
	int a_ant = 0;
	while (cont != k){
		c = a + b;
		a_ant = a;
		a = c;
		b = a_ant;
		cont++;
	}
	printf ("\nA:\t%d", a);
	printf ("\nB:\t%d\n", b);
	printf ("\nDividendo\tDivisor\t\tResto");
	euclides (a, b, 0);
}
/*Essa fun??o serve como "prova", isto ?, serve para realizar
o teste de mesa e comprovar que o mdc(a, b) realiza exatamente
as k divis?es pedidas*/
void euclides (int dividendo, int divisor, int resto){
	resto = dividendo % divisor;
	printf ("\n%d\t\t%d\t\t%d", dividendo, divisor, resto);
	if (resto == 0){
		printf ("\n\nMDC %c igual a : %d\n\n", 130, divisor);
	}
	else{
		euclides (divisor, resto, resto);
	}
}
