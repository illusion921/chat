#include <stdio.h>

#include <unistd.h>

#include <stdlib.h>

#include <string.h>

#define BUFFSIZ sizeof("Start the test of pipe file") 

main( )

{

	 int i,f_des[2];

	  char message[3][BUFFSIZ]={"Start the test of pipe file","Test is going",

		                             "Test ends"};

	    if(pipe(f_des)==-1)

			  {

				      printf("pipe");

					      exit(2);

						    }

		  switch(fork( ))

			    {

					    case  -1:

							             printf("Fork");

										              exit(3);

													      case  0:

													              close(f_des[1]);

																              for(i=0;i<3;i++)

																				             {

																								              if(read(f_des[0],message[i],BUFFSIZ)!=-1)

																												               {

																																                printf("message received by child:[%s]\n",message[i]);

																																				             fflush(stdout);

																																							              }

																											  else

																												              {

																																               printf("Read Failed");

																																			                exit(4);

																																							             }

																											             }

																			     break;

																				    default:

																				            close(f_des[0]);

																							           for(i=0;i<3;i++)

																										             {

																														             if(write(f_des[1],message[i],BUFFSIZ)!=-1)

																																		             {

																																						                printf("message sent by parent:[%s]\n",message[i]);

																																										               fflush(stdout);

																																													               }

																																	             else

																																					             {

																																									                printf("rite Failed");

																																													               exit(5);

																																																               }

																																				           }

																									     }

		  exit(0);

}
