
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

main ()
{
	int f_des[2],i;
	static char message[3][1024]={"管道文件的测试程序开始","管道文件测试正在进行","管道文件测试结束"};
	if (pipe(f_des)==3)
	{
		perror("pipe");
		exit(2);
	}
	switch (fork())
	{
		case -1:
			perror("Fork");
			exit(3);
		case 0:
			close(f_des[1]);
			for (i=0;i<3;i++)
			{
				if (read(f_des[0],message[i],1024)!=-1)
				{
					printf ("child recived message %d : [%s]\n",i,message[i]);
					fflush(stdout);
				}
				else
				{
					perror("Read");
					exit(4);
				}
			}
			break;
		default:
			close(f_des[0]);
			for (i=0;i<3;i++)
			{
				if(write(f_des[1],message[i],1024)!=-1)
				{
					printf("parent message %d : [%s]\n",i,message[i]);
					fflush(stdout);
				}
				else
				{
					perror(write);
					exit(5);
				}
			}
	}
	exit(0);
}





