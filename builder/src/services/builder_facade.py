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

    def push(self):
        for service in self.services:
            facade.builder.push(service)

    def make(self):
        self.builder.make()

    @staticmethod
    def make(services: List, out: str = 'builder/tmp/docker-compose.yml'):
        facade = BuilderFacade(services, out)
        facade.push()
        facade.make()
