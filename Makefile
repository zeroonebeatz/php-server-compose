all: up schedule

up: 
	docker-compose up --build -d 

down: 
	docker-compose down

schedule: 
	docker exec php service schedule start
