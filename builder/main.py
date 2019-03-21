#! /usr/bin/python3

from src.services.builder_facade import BuilderFacade

BuilderFacade.make([
    'nginx',
    'php',
    'nodejs',
    'mysql',
    'psql',
    'redis',
])
