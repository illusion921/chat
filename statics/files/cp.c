#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
	int fd1,fd2,n;
	char buf[512];
	if(argc<=2)
	{
		printf("you forgot to enter a filename.\n");
		exit(1);
	}
	fd1=open(argv[1],0);
	fd2=open(argv[2],2644);
	while ((n=read(fd1,buf,512))>0)
		write(fd2,buf,n);
	close(fd1);
	close(fd2);
	return 0;
}
