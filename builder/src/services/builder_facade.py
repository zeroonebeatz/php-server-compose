from typing import List
from src.services.builder import Builder


class BuilderFacade:
    conf = 'builder/store/compose.yml'  # compose configuration
    confd = 'builder/store/services/'  # services config dir
    builder = None
    services = []

    def __init__(self, services: List, out: str):
        self.services = services
        self.init_builder(out)

    def init_builder(self, out):
        compose = Builder.read_yaml(self.conf)
        self.builder = Builder(compose, self.confd, out)

    @staticmethod
    def make(services: List, out: str = 'builder/tmp/test.yml'):
        facade = BuilderFacade(services, out)

        for service in services:
            facade.builder.push(service)

        facade.builder.make()
