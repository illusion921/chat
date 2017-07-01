#include<signal.h>
#include<stdio.h>
#include<unistd.h>
int main()
{ int system(const char*string);
	void catchint(int signo);
	 int i;
	 signal(SIGINT,catchint);
	 for(i=1;i<=100;i++)
	 {printf("%d\n",i);
		 sleep(1);
	 }
	 printf("Exiting.\n");
	 exit(0);
}
  void catchint(int signo)
{/*signal(SIGINT,SIG_IGN);*/
	printf(system("date"));
	sleep(2);
	printf("CATCHINT,returning \n");
	signal(SIGINT,catchint()); 
	  }
