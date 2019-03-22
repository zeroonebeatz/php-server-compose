# Compose PHP server 
(for UNIX local development)

**app/**- projects parent dir

**builder/** - docker-compose builder dir

**docker/** - services config dir

## PHP

In docker/dockerfiles/php directory

    $ cp example.schedule_opts.sh schedule_opts.sh

And set your schedule services

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
For Linux set (lost after reboot):
    
    # sysctl -w vm.max_map_count=262144

or create sysctl config file /etc/sysctl.d/50-virtual.conf with parameters:

    vm.max_map_count=262144

# Configuration

## Requirement

- python3

## Build
Run command 

    $ cd builder/ && make

and chose needed containers

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
- elasticsearch
- memcached
- gearman

## TODO

- [ ] Cron
- [ ] Supervisord
- [ ] RabbitMQ
