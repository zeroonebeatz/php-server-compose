#! /usr/bin/python3

from src.cli.builder_cli import BuilderCli
from src.cli.builder_io import BuilderIO
from src.storages.services import Services
from src.storages.links import Links

available = (
    'nginx',
    'php',
    'nodejs',
    'mysql',
    'psql',
    'redis',
    'gearman',
    'memcached',
)

links = Links({
    'nginx': [
        'php'
    ],
    'php': [
        'mysql',
        'redis',
        'psql',
        'gearman',
        'memcached',
    ]
})

cli = BuilderCli(BuilderIO(Services(available, links)))
cli.run()
