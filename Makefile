all: up schedule

up: 
	PUID=$$(id -u) PGID=$$(id -g) docker-compose up --build -d 

down: 
	docker-compose down

restart: down up

schedule: 
	docker exec php service schedule start

php:
	docker exec -it php bash

nodejs:
	docker exec -it nodejs bash

mysql:
	docker exec -it mysql bash

mysql_create:
	@echo "New Database Name: "; \
	read dbName; \
	docker exec -it mysql sh -c 'echo "create database \`'$$dbName'\`" | mysql -uroot -plocal';

psql:
	docker exec -it psql bash

redis:
	docker exec -it redis /bin/sh

memcached:
	docker exec -it redis bash

gearman:
	docker exec -it gearman bash

test:
	@echo $$(id -u); \
	echo $$(id -g);
