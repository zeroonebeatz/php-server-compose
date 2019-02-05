# Compose PHP server for local development

**app/**- projects parent dir

**docker/** - services config dir

## Nginx

#### Create new servier
Add *.conf file to 'docker/nginx/conf.d/' dir

## MySQL

#### Create new database
    
    $ make mysql_create

## Nodejs

Connect to container, cd to project folder and use npm commands

# Usage

## Run

    $ make

## Down

    $ make down

## Connect to containers
    
    $ make CONTAINER_NAME


Containers:

- php
- nodejs
- mysql
- psql
- redis

