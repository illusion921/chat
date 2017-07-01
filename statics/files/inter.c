#include <signal.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
	void catchint(int signo);
	int i;
	int system(const char * string);
	signal(SIGINT,catchint);
	for (i=1;i<=100;i++)
	{
		printf ("num is %d\n",i);
		sleep (1);
	}
	printf ("exiting");
	exit(0);
}
void catchint(int signo)
{
	printf("\n CATCHINT;signo=%d\n",signo);
	printf("CATCHINT ,returning\n");
	printf("%s\n",system("date"));
}
