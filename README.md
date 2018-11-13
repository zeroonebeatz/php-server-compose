# STACK COMPOSE

**app/**- projects parent dir

**docker/** - services config dir

##Nginx

####Create new servier
Add *.conf file to 'docker/nginx/conf.d/' dir

## DB

## MySQL

####Create new database
Add *n*-databases.sql to 'docker/storages/mysql/init/' dir, with:

        CREATE DATABASE IF NOT EXISTS `primary`;
        CREATE DATABASE IF NOT EXISTS `secondary`;
