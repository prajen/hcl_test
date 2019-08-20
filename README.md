This reposistory contains two files Dockerfile and sourcecode file i.e mac_info_fetcher.py
In order to run a container with the program please execute following commands in sequence 
1.To build a docker image from the docker execute command:
   docker build </path/to/directory/containgfiles>
2.Execute docker image listing using 
   docker images
3.Spawn the docker container in daemonized mode using
   docker run -t -d <image_id>
4. List all running containers using
   docker ps
5. Connect to the container and spawn bash shell using
   docker exec -it 7b869f073bfb(container id) /bin/bash
6. Once connected to the container you will be propelled into "/usr/src/app/" diretcory  by virtue of WORKDIR directive of Dockerfile
   we can run the programe file using 
   ./mac_info_fetcher.py <mac_id>

Synopsis on the program:
 python program is written to accept atleast one command line parameter without which it will exit ,its programmed to try the code block and print out an error message incase of a connectivity issue .It will also appropritely complain if some invalid MAC address is entered.
 program is uses urllib library to make a GET request to public API of 
 
   

