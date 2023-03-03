# Dockerisation d'une application Flask et de sa base de donnée

### Initialization

Create a folder named "TD6_Docker" on your host. 
In this folder, open a command line tool and run the command : 
"git clone 

### Get the mongo and python image from Docker Public Registry

Run the command "docker pull mongo"
Run the command "docker pull python"

### Create your own Flask App image

Run the command "docker build -t "image-td6" .

### Create your network to allow Flask Container and Mongo container to exchange data

Run the command "docker network create --driver bridge network-td6
