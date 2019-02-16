# Compose PHP server 
(for UNIX local development)

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

## ElasticSearch

### Host machine configuration
For Linux set (lost on reboot):
    
    # sysctl -w vm.max_map_count=262144

or create sysctl config file /etc/sysctl.d/50-virtual.conf with parameters:

    vm.max_map_count=262144

# Usage

## Run

    $ make

with ElasticSearch

    $ make search

## Down

    $ make down

with ElasticSearch

    $ make down-search

## Connect to containers
    
    $ make CONTAINER_NAME


Containers:

- php
- nodejs
- mysql
- psql
- redis
- elasticsearch

## TODO

- [ ] Cron
- [ ] Supervisord
- [ ] RabbitMQ
