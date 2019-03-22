from typing import List
from src.services.builder import Builder
from src.storages.services import Services


class BuilderFacade:
    conf = 'store/compose.yml'  # compose configuration
    confd = 'store/services/'  # services config dir
    builder = None
    services = None

    def __init__(self, services: Services, out: str):
        self.services = services
        self.init_builder(out)

    def init_builder(self, out):
        compose = Builder.read_yaml(self.conf)
        self.builder = Builder(compose, self.confd, out)

    def push(self):
        for service in self.services.get():
            self.builder.push(service, self.get_links(service))

    def get_links(self, service: str):
        links = None

        if self.services.links.exists(service):
            s = self.services.get()
            sl = self.services.links.get(service)
            links = [l for l in sl if l in s]

        return links

    def make(self):
        self.builder.make()

    @staticmethod
    def build(services: Services, out: str = 'tmp/docker-compose.yml'):
        facade = BuilderFacade(services, out)
        facade.push()
        facade.make()
