all: up schedule

up: 
	docker-compose up --build -d 

down: 
	docker-compose down

schedule: 
	docker exec php service schedule start

php:
	docker exec -it php bash

mysql:
	docker exec -it mysql bash

psql:
	docker exec -it psql bash

redis:
	docker exec -it redis /bin/sh
