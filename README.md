# Dockerisation d'une application Flask et de sa base de donnée

### Initialization

Create a folder named "TD6_Docker" on your host. 
In this folder, open a command line tool and run the command : 
`git clone https://github.com/Timoth37/TD7_A4_CloudComputing.git`

### Get the mongo and python image from Docker Public Registry
In the same folder :
Run the command `docker pull mongo`
Run the command `docker pull python`

### Create your own Flask App image

Run the command `docker build -t "image-td6`.

### Create your network to allow Flask Container and Mongo container to exchange data

Run the command `docker network create --driver bridge network-td6`

### Make all containers thanks to Docker Compose

Run the command `docker compose up`

### You can populate the database

Run the command `docker exec -it td6_docker-mongodb-1 mongosh`

You should be in the mongo shell right now.
Run the command `use vetements`
Run the command `db.marques.insertMany([{"name" : "Nike", "price": 50, "country": "Etats-Unis"},
{"name" : "Adidas", "price": 60, "country": "Allemagne"},
{"name" : "Zara", "price": 40, "country": "Espagne"}])`

Your database is now populated. 

### Visit your work

On a browser, visit http://localhost:5000.\n On the main, route, you'll see the differents elements of your database. 
On the 
