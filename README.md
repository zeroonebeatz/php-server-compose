# PHP server compose

**app/**- projects parent dir

**docker/** - services config dir

## Nginx

#### Create new servier
Add *.conf file to 'docker/nginx/conf.d/' dir

## MySQL

#### Create new database
    
    $ make mysql_create

# Usage

## Run

        $ make

## Down

        $ make down

## Connect to containers
    
        $ make CONTAINER_NAME


Containers:

- php
- mysql
- psql
- redis

