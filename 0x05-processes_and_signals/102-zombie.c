#include <stdio.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - a program that creat 5 zombie processes an enter sleep loop
 * Return: always 0
 */

int main(void)
{
	int pid;

	int i = 0;

	while (!fork() && i < 5)
	{
		pid = getpid();
		printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	if (i == 0)
		infinite_while();
	return (0);
}

/**
 * infinte_while - infinte_while loop that sleep 1 second in
 *                 every itteration
 * Return: always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
