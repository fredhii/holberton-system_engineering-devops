#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - For every zombie process created,
 * it displays Zombie process created, PID: ZOMBIE_PID
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create 5 zombie processes
 * Return: Always 0
 */
int main(void)
{
	unsigned int i;
	size_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
