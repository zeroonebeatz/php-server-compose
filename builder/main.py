#! /usr/bin/python3

from src.cli.builder_cli import BuilderCli
from src.cli.builder_io import BuilderIO
from src.storages.services import Services

availble = (
    'nginx',
    'php',
    'nodejs',
    'mysql',
    'psql',
    'redis',
)

cli = BuilderCli(BuilderIO(Services(availble)))
cli.run()
