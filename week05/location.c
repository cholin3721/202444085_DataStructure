#include <stdio.h>
#include <stdlib.h>

int b = 99;  // global variable, static(data) memory

void test(int c) {  // local variable, stack memory
	printf("%x\n", &c);
}

int main() {
	int a = 7; // local variable, stack memory
	static int d = 8;  // static variable, static memory

    int* e = (int*)malloc(sizeof(int));  // heap memory

	printf("%x\n", &a);
	printf("%x\n", &b);
	test(55);
	printf("%x\n", &d);
    printf("%x\n", &e);  // stack memory
    printf("%x\n", e);
    
    free(e);
	return 0;
}