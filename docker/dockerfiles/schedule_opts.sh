#!/bin/bash

set -e

while [ true ]
do
    php /var/www/ttm/artisan schedule:run --verbose --no-interaction
    php /var/www/ttm/artisan queue:work --sleep=3 --tries=3 --timeout=60

    php /var/www/idel/artisan schedule:run --verbose --no-interaction
    php /var/www/idel/artisan queue:work --sleep=3 --tries=3 --timeout=60

    sleep 60
done
